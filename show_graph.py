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
    nx.draw(graph, with_labels=True, node_size=800)
    plt.axis('equal')
    plt.show()


def show_two_graphs(g1, g2):
    #generating edgelists readably by networkx
    g1edge_tuple_list = []
    for edge in g1.get_edges():
        edge_tuple = (edge.vertex_a.name, edge.vertex_b.name)
        g1edge_tuple_list.append(edge_tuple)
    g2edge_tuple_list = []
    for edge in g2.get_edges():
        edge_tuple = (edge.vertex_a.name, edge.vertex_b.name)
        g2edge_tuple_list.append(edge_tuple)

    #generating networkx graphs
    graph1 = nx.Graph()
    graph1.add_edges_from(g1edge_tuple_list)
    graph2 = nx.Graph()
    graph2.add_edges_from(g2edge_tuple_list)
    plt.clf()

    plt.subplot(121)
    plt.title('Graph1')
    nx.draw(graph1, node_color='lightblue', node_size=800, with_labels=True)
    plt.subplot(122)
    plt.title('Graph2')
    nx.draw(graph2, node_color='lightblue', node_size=800, with_labels=True)
    plt.axis('equal')
    plt.show()


def show_graph_comparable(g1, g2, g3):
    #generating edgelists readably by networkx
    g1edge_tuple_list = []
    for edge in g1.get_edges():
        edge_tuple = (edge.vertex_a.name, edge.vertex_b.name)
        g1edge_tuple_list.append(edge_tuple)
    g2edge_tuple_list = []
    for edge in g2.get_edges():
        edge_tuple = (edge.vertex_a.name, edge.vertex_b.name)
        g2edge_tuple_list.append(edge_tuple)
    g3edge_tuple_list = []
    for edge in g3.get_edges():
        edge_tuple = (edge.vertex_a.name, edge.vertex_b.name)
        g3edge_tuple_list.append(edge_tuple)

    #generating networkx graphs
    graph1 = nx.Graph()
    graph1.add_edges_from(g1edge_tuple_list)
    graph2 = nx.Graph()
    graph2.add_edges_from(g2edge_tuple_list)
    graph3 = nx.Graph()
    graph3.add_edges_from(g3edge_tuple_list)
    plt.clf()

    plt.subplot(221)
    plt.title('Graph1')
    nx.draw(graph1, node_color='lightblue', node_size=800, with_labels=True)
    plt.subplot(222)
    plt.title('Graph2')
    nx.draw(graph2, node_color='lightblue', node_size=800, with_labels=True)
    plt.subplot(223)
    plt.title('Graph3')
    nx.draw(graph3, node_color='lightblue', node_size=800, with_labels=True)
    plt.axis('equal')
    plt.show()

