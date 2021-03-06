import random
import itertools
import timeit
from .graph import *
from .edge import *
from .vertex import *

# --------------------------------------------------------------------------------------------------
# global Variables
random_pivot = False # beeinflusst wahl des pivot-elements in bronk()
longest_vlist = 0   # globale Variable, um nur größte Clique zurückzugeben
no_of_mcis = []     # sind essentiell für die folgenden Funktionen
checklabel = False  # wird True gesetzt wenn nur Knoten mit identischen Label gematcht werden dürfen
# --------------------------------------------------------------------------------------------------


# Neighborfunktion zur Berechnung des Modularen Produktes
def mod_neighbors(vertex, graph):
    neighbor_list = []
    for edge in graph.edges:
        if edge.vertex_a.name is vertex.name or edge.vertex_a.name == vertex.name:
            neighbor_list.append(edge.vertex_b)
        elif edge.vertex_b.name is vertex.name or edge.vertex_b.name == vertex.name:
            neighbor_list.append(edge.vertex_a)
        # elif edge.vertex_a.name.find(';') >= 0:
        #     if edge.vertex_a.name.split(';')[0] is vertex.name:
        #         neighbor_list.append(edge.vertex_b.vertex1)
        #     elif edge.vertex_b.name.split(';')[0] is vertex.name:
        #         neighbor_list.append(edge.vertex_a.vertex1)
    neighbor_list = list(dict.fromkeys(neighbor_list))  # cast to dict and back to list removes duplicates
    return neighbor_list



def modular_product(graph, graph1):
    m_vertex_list = []
    m_edge_list = []
    controlset = set()

    for i in itertools.product(graph.vertices, graph1.vertices): # Kartesisches Produkt der beiden Graphen -> wird in neuer Klasse abgespeicher
        if checklabel:
            if i[0].label == i[1].label:
                m_vertex_list.append(ModularVertex(str(i[0].name)+';'+str(i[1].name), i[0], i[1]))
        else:
            m_vertex_list.append(ModularVertex(str(i[0].name) + ';' + str(i[1].name), i[0], i[1]))

    for k in m_vertex_list:  # doppelte For-Schleife, um alle Beziehungen abzudecken
        for l in m_vertex_list:
            if k.get_vertex1() == l.get_vertex1() \
                    or k.get_vertex2() == l.get_vertex2(): # um zu verhindern, dass mit sich selbst parrt
                continue
            elif (k.get_vertex1() in mod_neighbors(l.get_vertex1(), graph) \
                    and k.get_vertex2() in mod_neighbors(l.get_vertex2(), graph1))\
                    or (k.get_vertex1() not in mod_neighbors(l.get_vertex1(), graph) \
                    and k.get_vertex2() not in mod_neighbors(l.get_vertex2(), graph1)):
                q = (k.get_name()+l.get_name())
                r = (l.get_name()+k.get_name())
                if q not in controlset and r not in controlset: # Sorgt dafür, dass keine Edge doppelt hinzugefügt wird.
                    controlset.add(q)
                    controlset.add(r)
                    m_edge_list.append(Edge(k, l))
    return Graph(m_vertex_list, m_edge_list)


# speichert die von bronk bisher längste gesehene Vertexlist
def determine_mcis(v_list):
    global longest_vlist, mcis, no_of_mcis
    if len(v_list) > longest_vlist:
        longest_vlist = len(v_list)
        mcis = v_list
    if len(v_list) == longest_vlist:
        no_of_mcis.append(longest_vlist)


def determine_no_of_mcis():
    amount = no_of_mcis.count(max(no_of_mcis))
    print('Found', amount, 'MCIS with', max(no_of_mcis), 'nodes.')


def print_vertex_list(v_list):
    if len(v_list) == longest_vlist:
        print('The following pairs were found (Graph 1 node ; Graph 2 node):')
        for v in range(0, (len(v_list))):
            print(v_list[v].name)
        print('\n')


def extract_v1(vlist):
    v1list = []
    for v in vlist:
        v1list.append(v.vertex1)
    return v1list


def extract_vPair(vlist, v1):
    for v in vlist:
        if v.vertex1 == v1:
            return v
    print('ERROR: no v2 found')


# nutzt einen Eingabegraphen aus modular_product() um der Vektorenliste aus bronk() die zugehörigen Kanten zuzuordnen
def build_graph_outof_vlist(vlist, graph1):
    print_vertex_list(vlist)
    new_graph = Graph()
    for v in vlist:
        new_graph.add_vertex(v)
    for v in vlist:
        for s in mod_neighbors(v.vertex1, graph1):
            if s in extract_v1(vlist):
                v_pair = extract_vPair(vlist, s)
                new_e = Edge(v, v_pair)
                edge_in_graph = False
                for e in new_graph.edges:
                    if (e.vertex_a.name == new_e.vertex_a.name and e.vertex_b.name == new_e.vertex_b.name)\
                            or (e.vertex_a.name == new_e.vertex_b.name and e.vertex_b.name == new_e.vertex_a.name):
                        edge_in_graph = True
                if edge_in_graph == False:
                    new_graph.add_edges(new_e)
    return new_graph


# function determines the neighbors of a given vertex
def neighbors(vertex):
    neighbor_list = []
    for edge in graph.edges:
        if edge.vertex_a is vertex:
            neighbor_list.append(edge.vertex_b)
        elif edge.vertex_b is vertex:
            neighbor_list.append(edge.vertex_a)
    neighbor_list = list(dict.fromkeys(neighbor_list))
    return neighbor_list


def count_and_sort(p, x):  # counts number of neighbors for each vertex and sorts
    w = p + x
    q = []
    for vertex in w:
        c = 0  # count variable for each vertex
        for i in range(0, len(graph.edges)):
            if graph.edges[i].vertex_a == vertex or graph.edges[i].vertex_b == vertex:
                c += 1
        q.append((vertex, c))
    j = sorted(q, key=lambda count_no: count_no[1])  # sorts List produced by count for count.number
    return j


def find_pivot(p, x):
    j = count_and_sort(p, x)
    p_with_pivot = p
    if len(j) > 0:
        pivot_vertex = j[len(j) - 1][0] # because j still consists of tuples we need [0]
        p_with_pivot = [val for val in p if val not in neighbors(pivot_vertex)]  # P\N(pivot)
    return p_with_pivot


def find_pivot_randomly(p, x):
    p_with_pivot = p
    pivot_list = p, x
    if len(pivot_list) > 0:
        pivot_vertex = random.randrange(len(pivot_list))
        p_with_pivot = [val for val in p if val not in neighbors(pivot_vertex)]  # P\N(pivot)
    return p_with_pivot


# the Bron-Kerbosch recursive algorithm
def bronk(r, p, x, firstrun):
    if random_pivot == False:
        p_with_pivot = find_pivot(p, x)
    else:
        p_with_pivot = find_pivot_randomly(p, x)
    if len(p) == 0 and len(x) == 0:
        if firstrun:
            determine_mcis(r)
        else:
            print_vertex_list(r)
        return
    for vertex in p_with_pivot[:]:
        r_new = r[:]
        r_new.append(vertex)
        p_new = [val for val in p if val in neighbors(vertex)]  # p intersects neighbor(vertex)
        x_new = [val for val in x if val in neighbors(vertex)]  # x intersects neighbor(vertex)
        bronk(r_new, p_new, x_new, firstrun)
        p.remove(vertex)
        x.append(vertex)

#
# start = timeit.default_timer()
# bronk([], graph.vertices, [])  # without pivot: 0.0001477
# stop = timeit.default_timer()
# print('time: ', stop - start)


def find_cliques(graphobject, firstrun):
    global graph
    graph = graphobject
    bronk([], graph.vertices, [], firstrun)


def find_mcis(graph1, graph2, checklabels=None, choose_pivot_randomly=None):
    global longest_vlist, checklabel, random_pivot
    if choose_pivot_randomly:
        random_pivot = True
    if checklabels:
        checklabel = True
    longest_vlist = 0
    mod_graph = modular_product(graph1, graph2)
    print('Finding Maximal Common Induced Subgraphs...')
    find_cliques(mod_graph, firstrun=True)
    # nach dem Durchlauf von find_clique() enthält die globale Variable mcis eine Vertexlist eines
    # maximum common induce subgraphs
    mcis_graph = build_graph_outof_vlist(mcis, graph1)
    determine_no_of_mcis()
    if len(no_of_mcis) > 1:
        more_output = input('Do you want to see all Maximal Common Induced Subgraphs? [y/n] ')
        if more_output == 'y':
            mod_graph = modular_product(graph1, graph2)
            print('Finding all maximal cliques...')
            find_cliques(mod_graph, firstrun=False)
            print('Done.')
        else:
            print('Bye.')
    return mcis_graph


#Dieser hier wird für den Guidetree als Alternative benötigt, da wir zur Konstruktion nie mehr
    #als den maximum subgraph brauchen.
def find_mcis_without_prompt(graph1, graph2, checklabels=None, choose_pivot_randomly=None, supergraph=False):
    global longest_vlist, checklabel, random_pivot
    if choose_pivot_randomly:
        random_pivot = True
    if checklabels:
        checklabel = True
    longest_vlist = 0
    mod_graph = modular_product(graph1, graph2)
    print('Finding Maximal Common Induced Subgraphs...')
    find_cliques(mod_graph, firstrun=True)
    mcis_graph = build_graph_outof_vlist(mcis, graph1)
    if graph1.name != None and graph2.name != None:
        mcis_graph.name = str('(' + graph1.name + ',' + graph2.name + ')')
        print("Graph created: " + str(mcis_graph.name))
    print('Vertices:', len(mcis_graph.vertices), 'Edges:', len(mcis_graph.edges))
    if supergraph == True:
        mcis_graph = add_supergraph_nodes(mcis_graph, graph1, graph2)
    return mcis_graph


# schnittmenge der nachbarn jedes knoten aus ankerset (hier vlist)
def check_neighbors_of_vectorlist(vlist):
    neighbor_list = []
    for vertex in vlist:
        for edge in graph.edges:
            if edge.vertex_a.name is vertex.name or edge.vertex_a.name == vertex.name:
                neighbor_list.append(edge.vertex_b)
            elif edge.vertex_b.name is vertex.name or edge.vertex_b.name == vertex.name:
                neighbor_list.append(edge.vertex_a)
    neighbor_list = list(dict.fromkeys(neighbor_list))  # entfernt duplikate
    for n in neighbor_list[:]:
        for a in vlist:
            if n not in neighbors(a):
                neighbor_list.remove(n)
                break
    return neighbor_list


def find_cliques_with_anker(graphobject, ankernodes, firstrun):
    print('Remember that your Anchor has to be a Common Induced Subgraph!')
    global graph
    graph = graphobject
    start_vertices = []
    start_vertices = check_neighbors_of_vectorlist(ankernodes)  # schnittmenge der nachbarn jedes knoten aus ankerset
    for v in start_vertices[:]:
        if v in ankernodes:
            start_vertices.remove(v)
    bronk(ankernodes, start_vertices, [], firstrun)


# wandelt die Anker-Eingabe von Strings in Knoten-Objekte um
def get_anker_nodes(modgraph, anker):
    ankernodes = []
    '''if anker.vertices equals modgraph.vertices.vertex1:
        add modgraph.vertices to anknodes'''
    for v in modgraph.vertices:
        if v.name in anker:
            ankernodes.append(v)
    return ankernodes


def find_ankered_mcis(graph1, graph2, anker, checklabels=None, choose_pivot_randomly=None, supergraph=False):
    '''
    :param graph1: als Graphobjekt
    :param graph2: als Graphobjekt
    :param anker: als Liste in folgendem Format ankerlist = ['v1;v2', 'v3;v4', ...]
    :return: graph-objekt
    '''
    global longest_vlist, checklabel, random_pivot
    if choose_pivot_randomly:
        random_pivot = True
    if checklabels:
        checklabel = True
    longest_vlist = 0
    mod_graph = modular_product(graph1, graph2)
    print('Finding Maximal Common Induced Subgraphs...')
    ankernodes = get_anker_nodes(mod_graph, anker)
    find_cliques_with_anker(mod_graph, ankernodes, firstrun=True)
    mcis_graph = build_graph_outof_vlist(mcis, graph1)
    print('Vertices:', len(mcis_graph.vertices), 'Edges:', len(mcis_graph.edges))
    if supergraph == True:
        mcis_graph = add_supergraph_nodes(mcis_graph, graph1, graph2)
    return mcis_graph

def add_supergraph_nodes(mcis, g1, g2):
    mcis_names = mcis.get_vertex_names()
    mcis_left = []
    mcis_right = []
    for name in mcis_names:
        mcis_split = name.split(';')
        mcis_left.append(mcis_split[0]),
        mcis_right.append(mcis_split[1])

    for name in g1.get_vertex_names():
       if name not in mcis_left:
           mcis.add_vertex(Vertex(name + ';_'))
           mcis_left.append(name)
    for name in g2.get_vertex_names():
       if name not in mcis_right:
           mcis.add_vertex(Vertex('_;' + name))
           mcis_right.append(name)

    for edge in g1.edges:
        v1, v2 = None, None
        for vertex in mcis.vertices:
            if edge.vertex_a.name == vertex.name.split(';')[0]:
                v1 = vertex
            if edge.vertex_b.name == vertex.name.split(';')[0]:
                v2 = vertex
            elif v1 != None and v2 != None:
                break
        e = Edge(v1, v2)
        mcis.add_edges(e)
    for edge in g2.edges:
        v1, v2 = None, None
        for vertex in mcis.vertices:
            if edge.vertex_a.name == vertex.name.split(';')[1]:
                v1 = vertex
            if edge.vertex_b.name == vertex.name.split(';')[1]:
                v2 = vertex
            elif v1 != None and v2 != None:
                break
        e = Edge(v1, v2)
        mcis.add_edges(e)

    return mcis

