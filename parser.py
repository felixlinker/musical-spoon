'''
Uses a graph-file as input and creates a Graph-Object out of Vertex and Edge Objects
'''
from vertex import Vertex
from edge import Edge
from graph import Graph


def parse(filename):

    # Properties of the graph. Characterized in the first block of a graph-file
    n_of_nodes = 0
    n_of_edges = 0
    nodes_label = False
    edges_label = False
    directed_graph = False

    # Vertex list is characterized in the 2nd block of a graph-file
    vertex_list = []

    # Edge list is characterized in the 3rd block of a graph-file
    edge_list = []

    # c is a counter to know in which block of the graph-file we are
    c = 0

    # dict für das Zugreifen auf die Vertices über ihre Namen
    vertex_dict = {}
    with open(filename, 'r') as file:
        file_content = file.readlines()
        for i in range(0, len(file_content)):
            temp = file_content[i].replace('\n', '').split(';')
            if temp == ['']:
                c += 1
            elif temp is not '' and c == 0:
                if temp[0] == '#nodes':
                    n_of_nodes = temp[1]
                elif temp[0] == '#edges':
                    n_of_edges = temp[1]
                elif temp[0] == 'Nodes labelled':
                    if temp[1] == 'True':
                        nodes_label = True
                    else:
                        nodes_label = False
                elif temp[0] == 'Edges labelled':
                    if temp[1] == 'True':
                        edges_label = True
                    else:
                        edges_label = False
                elif temp[0] == 'Directed graph':
                    if temp[1] == 'True':
                        directed_graph = True
                    else:
                        directed_graph = False
            elif c == 1:
                v = Vertex(temp[0])
                if nodes_label:
                     v.set_node_label(temp[1])
                vertex_list.append(v)
                vertex_dict.update({v.name: v})  # Vertex wird für Edges-Initialiserung gespeichert (Name=Key)
            elif c == 2:
                e = Edge(vertex_dict.get(temp[0]), vertex_dict.get(temp[1]))
                if edges_label:
                    e.set_label(temp[2])
                edge_list.append(e)

    graph = Graph(vertex_list, edge_list, n_of_nodes, n_of_edges, nodes_label, edges_label, directed_graph)
    return graph


def reverse_parser(g):
    '''
    :param g: Graph Object
    :return: .graph text
    USAGE run in terminal: python3 main.py >> newgraph.graph
    '''
    number_of_vertices = len(g.vertices)
    number_of_edges = len(g.edges)
    labelled_vertices = g.vertices_labelled
    labelled_edges = g.edges_labelled
    directed_graph = g.directed_graph

    Block2 = []
    Block3 = []

    # if-function is necessary because graph-Objects which were randomly created don't have labels
    if labelled_vertices != None:

        for vertex in g.vertices:
            if vertex.label != None:
                Block2.append(str(vertex.name)+';'+str(vertex.label)+';')
            else:
                Block2.append(str(vertex.name)+';')

        for edge in g.edges:
            if edge.label != None:
                Block3.append(str(edge.vertex_a.name)+';'+str(edge.vertex_b.name)+';'+str(edge.label))
            else:
                Block3.append(str(edge.vertex_a.name)+';'+str(edge.vertex_b.name))

    else:

        labelled_vertices = False
        labelled_edges = False
        directed_graph = False

        for vertex in g.vertices:
            Block2.append(str(vertex.name) + ';')

        for edge in g.edges:
            Block3.append(str(edge.vertex_a.name) + ';' + str(edge.vertex_b.name))

    print('#nodes;',number_of_vertices,'\n',\
          '#edges;',number_of_edges,'\n',\
          'Nodes labelled;',labelled_vertices,'\n',\
          'Edges labelled;', labelled_edges,'\n',\
          'Directed graph;',directed_graph,'\n', sep='')

    for word in Block2:
        print(word)
    print()
    for word in Block3:
        print(word)



