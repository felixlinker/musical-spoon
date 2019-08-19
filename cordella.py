# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:52:41 2019
@author: Arctandra
"""
from vertex import Vertex
from edge import Edge
from graph import Graph


def create_output_table(s1, s2, g_1, g_2):
    #Last things first: This function creates an output table from the matched nodes after completing the program, which contains
    #the original node names. 
    
    print("The following pairs were found (Graph 1 node; Graph 2 node):")
    if None not in s1:
        for i in range(0, len(s1)):
            print("Matching nodes: " + g_1[i] + ' ; ' + g_2[s1[i]])
    
    else:
        for i in range(0, len(s2)):
            print("Matching nodes: " + g_1[s2[i]] + ' ; ' + g_2[i])
    

# The next two functions just attempt to compile all followup or preceding nodes of a given vertex into one list.
# This uses the suggested changes to the edge and vertex classes (i.e. keeping a list of following and preceding nodes
# for every given node).
def find_successors(v):
    out = []

    if len(v.successors) != 0:
        for i in range(0, len(v.successors)):

            if v.successors[i].name not in out and v.successors[i].name != v.name:
                # Circular structures in graphs are a thing...I guess? So better keep this in to prevent adding the same index
                # several times.
                out.append(v.successors[i].name)
                out += find_successors(v.successors[i])
                
        
        out2 = []
        for i in range(0, len(out)):
            if out[i] not in out2:
                out2.append(out[i])
        
        return out2

    else:

        return []

def find_predecessors(v):
    in_ = []

    if len(v.predecessors) != 0:
        for i in range(0, len(v.predecessors)):

            if v.predecessors[i].name not in in_ and v.predecessors[i].name != v.name:
                in_.append(v.predecessors[i].name)
                in_ += find_predecessors(v.predecessors[i])

        in_2 = []
        for i in range(0, len(in_)):
            if in_[i] not in in_2:
                in_2.append(in_[i])
        
        return in_2

    else:

        return []
    
#The next function is mainly used for the alignment of chemical graphs - it ensures that only nodes representing the same type of 
#nuclei are mapped onto each other. Can be ignored for other graphs, since their node labels are "None".
def atomic_identity(x,y, g1, g2):
    if g1.vertices[x].label == g2.vertices[y].label:
        return True
    else:
        return False


#The following is the Feasibility function of the Cordella algorithm, required to check, if a proposed matching results in branches,
#that are not mutually exclusive.
def F(s, n, m, g1, g2):
    n_successors = []
    n_predecessors = []
    m_successors = []
    m_predecessors = []
    vertex_dict1 = {}
    vertex_dict2 = {}

    for vertex1 in g1.vertices:   # dict um über den Namen auf das Objekt zugreifen zu können
        vertex_dict1.update({vertex1.name: vertex1})
    for vertex2 in g2.vertices:
        vertex_dict2.update({vertex2.name: vertex2})

    n_successors.append(find_successors(vertex_dict1[n]))     # nachfolger und vorfolger werden gesucht
    n_predecessors.append(find_predecessors(vertex_dict1[n]))
    m_successors.append(find_successors(vertex_dict2[m]))
    m_predecessors.append(find_predecessors(vertex_dict2[m]))
    n_successors = sum(n_successors, [])                     # Braucht es, damit keine Listen in Listen gibt
    n_predecessors = sum(n_predecessors, [])
    m_successors = sum(m_successors, [])
    m_predecessors = sum(m_predecessors, [])
    count_n_succ = False               # Booleanwerte
    count_m_succ = False
    count_n_pred = False
    count_m_pred = False
    Tin_n = len(s[4])
    Tout_n = len(s[2])
    M_n = 0
    Tin_m = len(s[5])
    Tout_m = len(s[3])
    M_m = 0
    for n in n_successors:                           # guckt, ob alle Nachfolger von n auch ein Äquivalten in m haben
        if s[0][n] is not None:
            if s[1][s[0][n]] in m_successors:
                count_n_succ = True
            else:
                count_n_succ = False
                break

    for m in m_successors:                           # guckt, ob alle Nachfolger von m auch ein Äquivalten in n haben
        if s[1][m] is not None:
            if s[0][s[1][m]] in n_successors:
                count_m_succ = True
            else:
                count_m_succ = False
                break

    for n in n_predecessors:                         #same same
        if s[0][n] is not None:
            if s[1][s[0][n]] in m_successors:
                count_n_pred = True
            else:
                count_n_pred = False
                break

    for m in m_predecessors:                         #same same
        if s[1][m] is not None:
            if s[0][s[1][m]] in n_successors:
                count_m_pred = True
            else:
                count_m_pred = False
                break

    for i in range(0, len(s[0])):            # Berechnet die Knoten im Matching
        if s[0][i] is not None:
            M_n += 1

    for i in range(0, len(s[1])):
        if s[1][i] is not None:
            M_m += 1

    N_n = (len(g1.vertices) - M_n - Tin_n - Tout_n)
    N_m = (len(g2.vertices) - M_m - Tin_m - Tout_m)

    if Tout_n >= Tout_m and Tin_n >= Tin_m and N_n >= N_m \
    or count_m_pred and count_n_pred and count_n_succ and count_m_succ: # Steht jetzt für SubgraphIsomorphism
            return True
    else:
        return False

#A function that generates potential matching candidates from the remaining unmapped parts of the graph.
def P(s, g1, g2):
    # Empty lists are considered False in python.
    if len(s[2]) != 0 and len(s[3]) != 0:
        return [s[2], min(s[3])]
    # Reminder that the node names have to be parsed to indices (as integers) for this to work.
    elif len(s[4]) != 0 and len(s[5]) != 0:
        return [s[4], min(s[5])]

    else:
        N1 = []
        N2 = []

    for n in g1.vertices:
        if n.name not in s[1]:
            N1.append(n.name)

    for m in g2.vertices:
        if m.name not in s[0]:
            N2.append(m.name)

    return [N1, min(N2)]

#The core function of the Cordella algorithm - loops until one graph is successfully mapped onto the other.
def match(s, g1, g2):
    # First we have to fill the predecessor and successor vectors.
    
    print("Start matching round.")
    if None not in s[0] or None not in s[1]:
        # Since we assume a graph-graph or a graph-subgraph isomorphism, if either core_1 or core_2 are completely filled,
        # we can consider the matching process to be complete. Furthermore, one of the two has to be filled by the end.
        return [s[0], s[1]]

    else:

        # If someone has an idea how to do this without dragging g1, g2 into every new function, let me know.
        p = P(s, g1, g2)

        # I propose for simplicity to save the candidates returned by P(s) in two vectors (one containing all values of n,
        # one containing the value of m), which are then saved in the two-dimensional vector p. This way, we do not have
        # to save the carthesian product, because it implicitly follows from looping over all values n (m seems to always
        # be one value anyways). Careful, these have to be indices.
        for n in p[0]:

            if F(s, n, p[1], g1, g2):

                # The following just adds the indices of the newly matched nodes in the right positions in the core_1, core_2
                # vectors...
                s[0][n] = p[1]
                s[1][p[1]] = n

                # ...and remove those nodes from the predecessor and successor lists, since they are now part of M
                if n in s[2]:
                    s[2].remove(n)
                if n in s[4]:
                    s[4].remove(n)
                if p[1] in s[3]:
                    s[3].remove(p[1])
                if p[1] in s[5]:
                    s[5].remove(p[1])
                
                #Now we have to update the lists of successors and predecessors, that is we add all successors and predecessors
                #of the newly matched nodes that are not themselves matched:
                for a in find_successors(g1.vertices[n]):
                    if s[0][a] == None and a not in s[2]:
                        s[2].append(a)
                        
                for a in find_successors(g2.vertices[p[1]]):
                    if s[1][a] == None and a not in s[3]:
                        s[3].append(a)
                        
                for a in find_predecessors(g1.vertices[n]):
                    if s[0][a] == None and a not in s[4]:
                        s[4].append(a)
                        
                for a in find_predecessors(g2.vertices[p[1]]):
                    if s[1][a] == None and a not in s[5]:
                        s[5].append(a)
                        

                return match(s, g1, g2)


def initialize_match(s, g1, g2):
    # Basically, to save computation time later on, we have the program identify the first pair of matching nodes and then
    # immediately calculate all predecessors and successors of these two nodes. These lists will then be updated with each
    # future addition to the core_1 and core_2 vectors by removing the new matching nodes from the in_1, in_2, ou_1, out_2 vectors.
    print("Initialize first match...")
    found = False
    
    for n in g1.vertices:
        if found:
                break
        for m in g2.vertices:
            
            if F(s, n.name, m.name, g1, g2):
                
                #Here, the nodes that are predecessors or successors of a matched node are added to the respective vectors
                print("Found one")
                s[0][n.name] = g2.vertices[0].name
                s[1][g2.vertices[0].name] = n.name
                s[2] = find_successors(n)
                s[3] = find_successors(m)
                s[4] = find_predecessors(n)
                s[5] = find_predecessors(m)
                found = True
                break

    if found:
        return match(s, g1, g2)
    else:
        print("No initial match found.")


def Cordella(g1, g2):
    #For...."Implementation reasons"....if the graphs are not equal in size, the first one must be the bigger one. Otherwise, the
    #Feasibility function will act up. Therefore, if g1 is smaller than g2, their positions are swapped. 
    if len(g1.vertices) < len(g2.vertices):
        g1_temp = g1
        g1 = g2
        g2 = g1_temp
    
    #This should probably be changed later on, but we have to give our nodes unifiying names for comparability. But if we need
    #the names later on (for chemical graphs), here they are:
    hold_g1 = []
    hold_g2 = []
    #hold_g1.append(None)
    #hold_g2.append(None)
    
    for i in range(0, len(g1.vertices)):
        hold_g1.append(g1.vertices[i].name)
        g1.vertices[i].name = int(i)

    for i in range(0, len(g2.vertices)):
        hold_g2.append(g2.vertices[i].name)
        g2.vertices[i].name = int(i)

    # Initialize core_1, core_2 where indices of corresponding matched node is saved
    print("Initialize...")
    core_1 = [None] * len(g1.vertices)
    core_2 = [None] * len(g2.vertices)
    # Initialize in_1, out_1 and in_2, out_2 as empty - since there are no nodes matched right now, it is impossible
    # to define predecessor or successor nodes at initialization.
    in_1 = []
    in_2 = []
    out_1 = []
    out_2 = []

    # We shall save these 6 vectors as a list to simplify the assignment of values. It would be paramount to
    # never change their order, please. As in, never ever.
    s = [core_1, core_2, out_1, out_2, in_1, in_2]
    print("Initialize complete.")
    # Call the Matching function
    cord =  initialize_match(s, g1, g2)
    
    #Make use of the output:
    if cord == None:
        print("Invalid pairs - no isomorphism could be found.")
    else:
        create_output_table(cord[0], cord[1], hold_g1, hold_g2)

