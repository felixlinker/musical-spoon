# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:17:23 2019


"""

import numpy as np
from vertex import Vertex
from edge import Edge
from graph import Graph


def random_graph(lower_node_limit, upper_node_limit, deletion_chance):
    
    #Note: It is absolutely crucial, that the deletion_chance parameter is a value between 0 and 1. Bad things happen otherwise. 
    #The deletion chance corresponds to the probability, that a given possible edge does NOT exist in the graph and is universal for all edges. 
    
    n_nodes = 0
    vertex_list = []
    edge_list =[]
    
    #Number of nodes 
    n_nodes = np.random.randint(lower_node_limit +1, upper_node_limit +2)
    
    #Generate a set of vertices - at the moment without label   
    for i in range(0, n_nodes):
        node = Vertex(str(i))
        vertex_list.append(node)
    
    #Generate a set of edges
    edge_matrix = np.zeros((n_nodes+1, n_nodes+1))
    
    for i in range(0, n_nodes):
        edge_matrix[i][0] = i
        edge_matrix[0][i] = i
        

    for i in range(1, n_nodes):
                
            if i+1 < n_nodes:
                x = np.random.randint(i+1, n_nodes)
                if edge_matrix[x][i] == 0 and (100-deletion_chance*100) > np.random.randint(0, 101):
                    e = Edge(vertex_list[i], vertex_list[x])
                    edge_matrix[i][x] = 1
                    edge_matrix[x][i] = 1
                    edge_list.append(e)

    #Create the Graph
    g = Graph(vertex_list, edge_list)
    return g

def random_chess_graph(lower_node_limit, upper_node_limit, deletion_chance):
    
    #Note: It is absolutely crucial, that the deletion_chance parameter is a value between 0 and 1. Bad things happen otherwise. 
    #The deletion chance corresponds to the probability, that a given possible edge does NOT exist in the graph and is universal for all edges. 
    
    n_nodes = 0
    vertex_list = []
    edge_list =[]
    
    #Number of nodes ------------------------------------------------
    n_nodes = np.random.randint(lower_node_limit +1, upper_node_limit +2)
     
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
    #deletion_chance parameter.
    
    for i in range(0, side_length):
        for j in range(0, side_length):      
            
            if i+j+1+i*(side_length-1) < len(vertex_list) and j < side_length-1 and (100-deletion_chance*100) > np.random.randint(0, 101):
                edge_list.append(Edge(vertex_list[i+j+i*(side_length-1)], vertex_list[i+j+1+i*(side_length-1)]))
                #print(str(vertex_list[i+j+i*(side_length-1)].name) + ',' + str(vertex_list[i+j+1+i*(side_length-1)].name))
            if i+1+j + (i+1)*(side_length-1) < len(vertex_list) and (100-deletion_chance*100) > np.random.randint(0, 101):
                edge_list.append(Edge(vertex_list[i+j+i*(side_length-1)], vertex_list[i+1+j + (i+1)*(side_length-1)]))
                #print(str(vertex_list[i+j+i*(side_length-1)].name) + ',' + str(vertex_list[i+1+j + (i+1)*(side_length-1)].name))
                #Note: Given how the vertex_list is filled, the distance to the vertex n(i,j+1) is always constant


    return Graph(vertex_list, edge_list)
           

def locate_vertex(vertex_list, name):
    
    #Evtl Binärsuche implementieren
    for a in range(0, len(vertex_list)):
        if vertex_list[a].name == name:
            return a
    #Try-catch-Block wäre angebracht
    return -1

def random_triangular_graph(lower_node_limit, upper_node_limit, deletion_chance):
    
    n_nodes = 0
    vertex_list = []
    edge_list = []
    edge_names = []
    
    #Number of nodes
    nodes_limit = np.random.randint(lower_node_limit +1, upper_node_limit +2)
    
    #For the graph, we want a triangle with sides of equal length, therefore:
    side_length = 1
    while n_nodes <= nodes_limit:
        n_nodes += side_length
        side_length += 1
    
    side_length -= 1
    
    #The triangular graph is best envisioned as if it had 3 dimensions/is a 3 dimensional object compressed to a planar space...
    for x in range(0, side_length):
        for y in range(0, side_length):
            for z in range(0, side_length):
                
                if (x + y + z) == side_length-1:
                    node_identity = str(x) + '_' + str(y) + '_' + str(z)
                    print(node_identity)
                    vertex_list.append(Vertex(node_identity))
                
    #In a triangular graph, the potential partners for edge construction of a given node n are: n(+1,+0,-1), n(+1,-1,+0), 
    #n(+0,-1,+1), n(-1,+0,+1), n(-1,+1,0), n(+0,+1,-1). Given that these vertices exist, of course.
    for vertex in vertex_list:
        coordinates = (vertex.name.split('_'))
        for a in range(0, len(coordinates)):
            coordinates[a] = int(coordinates[a])
        
        if coordinates[0]-1 >= 0:
            if coordinates[1]+1 < side_length and (100-deletion_chance*100) > np.random.randint(0, 101):
                v_index = locate_vertex(vertex_list, str(coordinates[0]-1)+'_'+str(coordinates[1]+1)+'_'+str(coordinates[2]+0))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                
            if coordinates[2]+1 < side_length and (100-deletion_chance*100) > np.random.randint(0, 101):
                v_index = locate_vertex(vertex_list, str(coordinates[0]-1)+'_'+str(coordinates[1]+0)+'_'+str(coordinates[2]+1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
            
        if coordinates[1]-1 >= 0:
            if coordinates[0]+1 < side_length and (100-deletion_chance*100) > np.random.randint(0, 101):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+1)+'_'+str(coordinates[1]-1)+'_'+str(coordinates[2]+0))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                    
            if coordinates[2]+1 < side_length and (100-deletion_chance*100) > np.random.randint(0, 101):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+0)+'_'+str(coordinates[1]-1)+'_'+str(coordinates[2]+1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                    
        if coordinates[2]-1 >= 0:
            if coordinates[0]+1 < side_length and (100-deletion_chance*100) > np.random.randint(0, 101):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+1)+'_'+str(coordinates[1]+0)+'_'+str(coordinates[2]-1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))
                    
            if coordinates[1]+1 < side_length and (100-deletion_chance*100) > np.random.randint(0, 101):
                v_index = locate_vertex(vertex_list, str(coordinates[0]+0)+'_'+str(coordinates[1]+1)+'_'+str(coordinates[2]-1))
                if not (str(vertex_list[v_index].name + '_' + vertex.name)) in edge_names and v_index > -1:
                    edge_list.append(Edge(vertex, vertex_list[v_index]))
                    edge_names.append(str(vertex.name + '_' + vertex_list[v_index].name))


    return Graph(vertex_list, edge_list)
    

