import networkx as nx
import matplotlib.pyplot as plt


def show_graph(g):

    # generates edgelist which is readable by networkx
    edge_tuple_list = []
    for edge in g.get_edges():
        edge_tuple = (edge.vertex_a.name, edge.vertex_b.name)
        edge_tuple_list.append(edge_tuple)
    
    graph = nx.Graph()
    graph.add_edges_from(edge_tuple_list)
    nx.draw(graph, with_labels=True)
    plt.show()

