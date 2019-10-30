# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:17:23 2019
"""

import numpy as np
from vertex import Vertex
from edge import Edge
from graph import Graph


def random_graph(lower_node_limit=1, upper_node_limit=10, more_edges = False):
    
    #Note: It is absolutely crucial, that the deletion_chance parameter is a value between 0 and 1. Bad things happen otherwise. 
    #The deletion chance corresponds to the probability, that a given possible edge does NOT exist in the graph and is universal for all edges. 
    
    n_nodes = 0
    vertex_list = []
    edge_list =[]
    
    #Number of nodes 
    if lower_node_limit == upper_node_limit:
        n_nodes = lower_node_limit
    else:
        n_nodes = np.random.randint(low = lower_node_limit, high = upper_node_limit)
    
    #Generate a set of vertices - at the moment without label   
    for i in range(0, n_nodes):
        node = Vertex(str(i))
        vertex_list.append(node)   
    
    #Generate a set of edges
    edge_matrix = np.zeros((n_nodes+1, n_nodes+1))

    #Edges are generated in correspondence to a matrix, which contains all possible combinations of vertices. Then edges are added at random. The 
    #exact chance for addition of an edge was based on a testing period during development.
    for i in range(0, n_nodes):
                
            if i+1 < n_nodes:
                x = np.random.randint(low = i+1, high = n_nodes)
                if edge_matrix[x][i] == 0 and (90) > np.random.randint(low=1, high=100):
                    e = Edge(vertex_list[i], vertex_list[x])
                    edge_matrix[i][x] = 1
                    edge_matrix[x][i] = 1
                    edge_list.append(e)
                if more_edges:
                    x = np.random.randint(low = i+1, high = n_nodes)
                    if edge_matrix[x][i] == 0 and (90) > np.random.randint(low=1, high=100):
                        e = Edge(vertex_list[i], vertex_list[x])
                        edge_matrix[i][x] = 1
                        edge_matrix[x][i] = 1
                        edge_list.append(e)

    for n in range(0, len(vertex_list)):
        if 1 not in edge_matrix[n]:
            s = False
            while s == False:
                x = np.random.randint(0, n_nodes)
                if x != n:
                    edge_list.append(Edge(vertex_list[i], vertex_list[x]))
                    s = True

    #Create the Graph.
    g = Graph(vertex_list, edge_list)
    return g
    
    
    
def random_chess_graph(lower_node_limit=4, deletion_chance = 0, name=None):
    
    #Note: It is absolutely crucial, that the deletion_chance parameter, if given, is a value in the interval (0, 1). Bad things happen otherwise. 
    #The deletion chance corresponds to the probability, that a given possible edge does NOT exist in the graph and is universal for all edges. 
    
    n_nodes = 0
    vertex_list = []
    edge_list =[]
    
    #Number of nodes ------------------------------------------------

    n_nodes = lower_node_limit
        #For simplicity, we scout for the next value with a square root that is a natural number. 
    #This smoothes the for-loops later on, as we don't have to account for weird appdendices 
    while (np.sqrt(n_nodes) % 1 != 0):
       n_nodes += 1

    side_length = int(np.sqrt(n_nodes))
    
    for i in range(0, side_length):
        for j in range(0, side_length):
            node_identity = str(i) + '_' + str(j)
            new_node = Vertex(node_identity)
            vertex_list.append(new_node)
    
    #Now for the edges. In this type of graph, only edges between direct neighbors on the "chessboard"
    #may exist, that is to say for n(i, j) potential edges could be formed with n(i-1, j),
    #n(i, j-1), n(i+1, j), n(i, j+1). The chance that a certain edge does NOT exist is given by the 
    #deletion_chance parameter, if one is given at all.
    
    for i in range(0, side_length):
        for j in range(0, side_length):      
            
            if i+j+1+i*(side_length-1) < len(vertex_list) and j < side_length-1 and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                edge_list.append(Edge(vertex_list[i+j+i*(side_length-1)], vertex_list[i+j+1+i*(side_length-1)]))
                #print(str(vertex_list[i+j+i*(side_length-1)].name) + ',' + str(vertex_list[i+j+1+i*(side_length-1)].name))
            if i+1+j + (i+1)*(side_length-1) < len(vertex_list) and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                edge_list.append(Edge(vertex_list[i+j+i*(side_length-1)], vertex_list[i+1+j + (i+1)*(side_length-1)]))
                #print(str(vertex_list[i+j+i*(side_length-1)].name) + ',' + str(vertex_list[i+1+j + (i+1)*(side_length-1)].name))
                #Note: Given how the vertex_list is filled, the distance to the vertex n(i,j+1) is always constant


    return Graph(vertex_list, edge_list, name=name)
           

def locate_vertex(vertex_list, name):
    
    #Evtl Binärsuche implementieren
    for a in range(0, len(vertex_list)):
        if vertex_list[a].name == name:
            return a
    return -1

def random_triangular_graph(lower_node_limit=3, deletion_chance = 0):
    
    n_nodes = 0
    vertex_list = []
    edge_list = []
    edge_names = []
    
    #Number of nodes
    nodes_limit = lower_node_limit      
    #For the graph, we want a triangle with sides of equal length, therefore:
    side_length = 1
    while n_nodes < nodes_limit:
        n_nodes += side_length
        side_length += 1
    
    side_length -= 1
    
    #The triangular graph is best envisioned as if it had 3 dimensions/is a 3 dimensional object compressed to a planar space.
    for x in range(0, side_length):
        for y in range(0, side_length):
            for z in range(0, side_length):
                
                if (x + y + z) == side_length-1:
                    node_identity = str(x) + '_' + str(y) + '_' + str(z)
                    vertex_list.append(Vertex(node_identity))
                
    #If we treat the Object as a pseudo 3D-Object, then in a triangular graph, the potential partners for edge construction of a given node n are: n(+1,+0,-1), n(+1,-1,+0), 
    #n(+0,-1,+1), n(-1,+0,+1), n(-1,+1,0), n(+0,+1,-1). Given that these vertices exist, of course.
    for vertex in vertex_list:
        coordinates = (vertex.name.split('_'))
        for a in range(0, len(coordinates)):
            coordinates[a] = int(coordinates[a])
        
        if coordinates[0]-1 >= 0:
            if coordinates[1]+1 < side_length and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                v_index = locate_vertex(vertex_list, str(coordinates[0]-1)+'_'+str(coordinates[1]+1)+'_'+str(coordinates[2]+0))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                
            if coordinates[2]+1 < side_length and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                v_index = locate_vertex(vertex_list, str(coordinates[0]-1)+'_'+str(coordinates[1]+0)+'_'+str(coordinates[2]+1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
            
        if coordinates[1]-1 >= 0:
            if coordinates[0]+1 < side_length and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+1)+'_'+str(coordinates[1]-1)+'_'+str(coordinates[2]+0))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                    
            if coordinates[2]+1 < side_length and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+0)+'_'+str(coordinates[1]-1)+'_'+str(coordinates[2]+1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                    
        if coordinates[2]-1 >= 0:
            if coordinates[0]+1 < side_length and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+1)+'_'+str(coordinates[1]+0)+'_'+str(coordinates[2]-1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                    
            if coordinates[1]+1 < side_length and (100-deletion_chance*100) > np.random.randint(low=1, high=100):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+0)+'_'+str(coordinates[1]+1)+'_'+str(coordinates[2]-1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))


    return Graph(vertex_list, edge_list)
    

def complete_graph(nodes= 10):
    
    v_list = []
    e_list = []
    for i in range(0, nodes):
        v_list.append(Vertex(i))
    for i in range(0, nodes-1):
        for x in range(i+1, nodes):
            e_list.append(Edge(v_list[i], v_list[x]))
    return Graph(v_list, e_list)


#Just a small tool to randomly delete edges in a graph based on chance
def cut_edges(graph, chance = 0.1):
    
    g = graph
    
    for e in g.edges:
        if (100-chance*100) < np.random.randint(low=1, high=100):
            e.cut_successors()
            e.cut_predecessors()
            g.edges.remove(e)
    
    return g

def add_random_nodes(graph, n=1):
    v_list = []
    e_list = []
    for i in range(0,n):
        v_list.append(Vertex(('add_' + str(i))))
    
    for i in range(0, len(v_list)):
        e_list.append(Edge(v_list[i], g.vertices[np.random.randint(low = 0, high = len(g.vertices))]))
    
    for i in range(0, len(v_list)):
        g.vertices.append(v_list[i])
        g.edges.append(e_list[i])
    return g