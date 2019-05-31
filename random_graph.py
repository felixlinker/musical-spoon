# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:17:23 2019


"""

#TODO: -Bei Block2 wird ein ; zu viel eingetragen, wird morgen in Ordnung gebracht
        
#      -Implementierung gerichteter Graphen

import numpy as np
from vertex import Vertex
from edge import Edge
from graph import Graph


def random_graph(lower_node_limit, upper_node_limit, nodes_labeled, edges_labeled):
    
    n_nodes = 0
    n_edges = 0
    vertex_list = []
    edge_list =[]
    
    #Number of nodes 
    n_nodes = np.random.randint(lower_node_limit, upper_node_limit +1)
    
    #Number of edges
    edges_limit = (n_nodes*(n_nodes -1))/2
    n_edges = np.random.randint(1, edges_limit +1)
    
    #Generate a set of vertices - at the moment without label
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(0, n_nodes):
        
        if i < len(alphabet):
            c = alphabet[i]
            node = Vertex(c)
            vertex_list.append(node)
        else:
            node_name_over_z = "z"
            node_name_over_z += str(i)
            node = Vertex(node_name_over_z)
            vertex_list.append(node)
    
    #Generate a set of edges
    edge_matrix = np.zeros((n_nodes+1, n_nodes+1))
    
    for i in range(0, n_nodes):
        edge_matrix[i][0] = i
        edge_matrix[0][i] = i
        
   # while n_edges > 0:
    for i in range(1, n_nodes):
                
            if i+1 < n_nodes:
                x = np.random.randint(i+1, n_nodes)
                if edge_matrix[x][i] == 0 and n_edges > 0:
                    e = Edge(vertex_list[i], vertex_list[x])
                    edge_matrix[i][x] = 1
                    edge_matrix[x][i] = 1
                    print(edge_matrix)
                    edge_list.append(e)
                    n_edges -= 1


    #Create the Graph
    g = Graph(vertex_list, edge_list)
    return g
            
           

def write_random_graph(lower_node_limit, upper_node_limit, nodes_labeled, edges_labeled, directed):
    
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

