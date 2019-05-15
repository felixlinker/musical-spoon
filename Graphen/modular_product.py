# -*- coding: utf-8 -*-
"""

"""
from Vertex import Vertex
from Edge import Edge
from Graph import Graph

def get_modular_edge(v1, v2, graph1, graph2):
    
    #checks if there are edges for one, none or all corresponding vertices in the origin graphs and creates a result edge
    c = 0
    names_v1, names_v2 = v1.name.split('_'), v2.name.split('_')
    
    for e in graph1.edges:
        if (e.vertex_a.name == names_v1[0] and e.vertex_b.name == names_v2[0]) or (e.vertex_b.name == names_v1[0] and e.vertex_a.name == names_v2[0]):
            c += 1
    for e in graph2.edges:
        if (e.vertex_a.name == names_v1[1] and e.vertex_b.name == names_v2[1]) or (e.vertex_b.name == names_v1[1] and e.vertex_a.name == names_v2[1]):
            c += 1
    if (c == 0 or c >= 2) and v1.name != v2.name and names_v1[0] != names_v2[0] and names_v1[1] != names_v2[1]:
        modular_edge = Edge(v1, v2)
        return modular_edge
    else:
        return None
        

def modular_product(g1, g2):
    
    vertex_list = []
    edge_list = []
    
    #cartesian product of the vertices
    for ga in g1.vertices:
        for gb in g2.vertices:
            
            vname = ""
            vname += ga.name
            vname += '_'
            vname += gb.name
            vertex_list.append(Vertex(vname))
    
    for i in range(0, len(vertex_list)):
        for l in range(i, len(vertex_list)):
            edge = get_modular_edge(vertex_list[i], vertex_list[l], g1, g2)
            if edge is None:
                continue
            else:
                edge_list.append(edge)
                 
    
    modular_graph = Graph(vertex_list, edge_list)
    return modular_graph
    