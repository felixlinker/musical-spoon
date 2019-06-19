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
    

def write_random_graph(lower_node_limit, upper_node_limit, nodes_labeled, edges_labeled, directed):
    #NOTE: For now using this method is discouraged. 
    
    targetfile = open("randomgraph.graph", "a")
    block1 = ""
    block2 = ""
    block3 = ""
    
    #Write the number of nodes
    nodes = np.random.randint(lower_node_limit, upper_node_limit +1)
    block1 += "#nodes;"
    block1 += str(nodes)
    
    #Decide on a number of edges 
    edges_limit = (nodes*(nodes -1))/2
    edges = np.random.randint(1, edges_limit +1)
    block1 += "#edges;"
    block1 += str(edges)

     #nodes are labeled?
    block1 += "Nodes labelled;"
    if nodes_labeled == True:
        block1 += "True"
    else:
        block1 += "False"

    #Edges are labeled?
    block1 += "Edges labelled;"
    if edges_labeled == True:
        block1 += "True"
    else:
        block1 += "False"

    #This graph is directed?
    block1 += "Directed graph;"
    block1 += str(directed)
    block1 += '\n'
    
    #nodes/edges
    node_list = np.arange(1, nodes+1)
    edge_list = np.zeros((len(node_list), len(node_list)))
    for i in range(len(node_list)):
        edge_list[i][0] = i
        edge_list[0][i] = i
    
    while edges > 0:
        for i in range(len(node_list)):
            for b in range(len(node_list)):
                if edge_list[i][b] == 0 and i < b:
                    x = np.random.randint(0,2) > 0
                    if x > 0:
                        edge_list[i][b] = b
                        edge_list[b][i] = i
                        edges -= 1
                    else:
                        continue
    #create block2 for vertices
    #create block3 for the edges
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(node_list)):
        
        
        block2 += str(i+1)
        block2 += ';'
        block2 += str(alphabet[i])
        block2 += ';'
        
        for b in range(len(node_list)):
            
            if edge_list[i][b] != 0:
                
                block2 += str(int(edge_list[0][b])+1)
                block2 += ';'
               
                block3 += str(int(edge_list[i][0])+1)
                block3 += ';'
                block3 += str(int(edge_list[0][b])+1)
                
    block2 += '\n'
    block3 += '\n'
    
    #print(block1)
    #print(block2)
    #print(block3)

    targetfile.write(block1)
    targetfile.write(block2)
    targetfile.write(block3)    
    targetfile.close()

def reverse_parser(g):
    #TODO work in progress
    '''
    :param g: Graph Object
    :return: .graph text file
    '''
    number_of_vertices = len(g.vertices)
    number_of_edges = len(g.edges)
    labelled_vertices = g.vertices_labelled
    labelled_edges = g.edges_labelled
    directed_graph = g.directed_graph

    Block2 = []
    Block3 = []


    for vertex in g.vertices:
        Block2.append(vertex.name+';')

    for edge in g.edges:
        Block3.append(edge.vertex_a.name+';'+edge.vertex_b.name+';'+edge.label)


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

