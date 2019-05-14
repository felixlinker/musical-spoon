from Parser import parse
import itertools
from ModularVertex import ModularVertex
from Edge import Edge
from Graph import Graph

graph = parse('Graphen/WikipediaGraph.graph')
graph1 = parse('Graphen/WikipediaGraph.graph')

def neighbors(vertex, graph):
    neighbor_list = []
    for edge in graph.edges:
        if edge.vertex_a is vertex:
            neighbor_list.append(edge.vertex_b)
        elif edge.vertex_b is vertex:
            neighbor_list.append(edge.vertex_a)
    return neighbor_list

def Modulares_Produkt(graph,graph1):
    m_vertex_list = []
    m_edge_list = []
    controlset = set()

    for i in itertools.product(graph.vertices, graph1.vertices): # Kartesisches Produkt der beiden Graphen -> wird in neuer Klasse abgespeicher
        m_vertex_list.append(ModularVertex(i[0].name+i[1].name, i[0], i[1]))

    for k in m_vertex_list:  # doppelte For-Schleife, um alle Beziehungen abzudecken
        for l in m_vertex_list:
            if k.get_vertex1() == l.get_vertex1() \
                    or k.get_vertex2() == l.get_vertex2(): # um zu verhindern, dass mit sich selbst parrt
                continue
            elif k.get_vertex1() in neighbors(l.get_vertex1(), graph) \
                    and k.get_vertex2() in neighbors(l.get_vertex2(), graph1)\
                    or k.get_vertex1() not in neighbors(l.get_vertex1(), graph) \
                    and k.get_vertex2() not in neighbors(l.get_vertex2(), graph1):
                q = (k.getname()+l.getname())
                r = (l.getname()+k.getname())
                if q not in controlset and r not in controlset: # Sorgt dafür, dass keine Edge doppelt hinzugefügt wird.
                    controlset.add(q)
                    controlset.add(r)
                    m_edge_list.append(Edge(k, l, k.getname()+' '+l.getname()))

    return Graph(m_vertex_list, m_edge_list)