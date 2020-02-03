# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:57:44 2019
@author: Christopher
"""

import numpy as np
from vertex import Vertex
import show_graph
from edge import Edge
from graph import Graph
from bronk_pivot import find_mcis_without_prompt

def call_subgraph_algorithm(g1, g2, supergraph=True):
        
    #This is a placeholder right now, but this function handles the pipeline to the 
    #actual alignment algorithms later on.
    mcis_sup = find_mcis_without_prompt(g1, g2, supergraph=True)
    for v in mcis_sup.vertices:
        v.name = v.name.replace(';', ':')
    
    return mcis_sup
    
    
def score_similarity(g1, g2):
    #This will of course need to be reworked to include a function to judge the relative
    #similarityof two graphs...
    return abs(len(g1.edges) - len(g2.edges))

def add_missing_nodes(mcis, g1, g2):
    return None

class guide_tree:
    
    def __init__(self, graph_list: [] = None, construct_tree = True,  name = None, supergraph = True):
        
        #If a tree should be build as a graph, the graphs will need to have names.
        tree_nodes = []
        tree_branches = []
        self.graph_list = graph_list
        self.construct_tree = construct_tree
        self.name = name
        self.supergraph = supergraph
        
        #This starts building the leaves for the output guide tree:
        if construct_tree == True:
            vertex_dict = {}
            for i in range(0, len(graph_list)):
                v = Vertex(graph_list[i].name)
                tree_nodes.append(v)
                vertex_dict.update({v.name: v})
        
        score_matrix = []
        for n in range(0, len(graph_list)):
            vec = []
            score_matrix.append(vec) #just make enough entries in the matrix
            for b in range(0, len(graph_list)):
                if n != b:
                    score_matrix[n].append(score_similarity(graph_list[n], graph_list[b]))
                    
                else:
                    score_matrix[n].append(9999)
        #---------------------------------------------------          
        
        pairs = []
        hold_last = None

        for n in range(0, len(graph_list)):
            minimal = 9999
            minimal_pos = [None, None]
            if graph_list[n] != None:
                X = 0
                #Just a cleanup, in case we have an uneven number ...
                if len(pairs) * 2 + 1 == len(graph_list):
                    hold_last = graph_list[n]
                    break
                    

                for x in range(n, len(score_matrix[n])):
                    if score_matrix[n][x] < minimal and graph_list[x] != None:
                        minimal = score_matrix[n][x]
                        minimal_pos[0] = (graph_list[n])
                        minimal_pos[1] = (graph_list[x])
                        X = x
                pairs.append((minimal_pos))
                graph_list[X] = None
                
        #Just a cleanup, in case we have an uneven number ...
        l = len(pairs)
        
        while l > 1 or hold_last != None:
            tmp = []
            for n in range(0, len(pairs)):
                a = call_subgraph_algorithm(pairs[n][0], pairs[n][1], self.supergraph)
                show_graph.show_graph(pairs[n][0])
                show_graph.show_graph(pairs[n][1])
                show_graph.show_graph(a)
                tmp.append(a)
                #Continue building the graph representation of the tree, if needed:
                if construct_tree == True:
                    v = Vertex(str(a.name))
                    tree_nodes.append(v)
                    vertex_dict.update({v.name: v})
                    e1 = Edge(vertex_dict.get(pairs[n][0].name), v)
                    e2 = Edge(vertex_dict.get(pairs[n][1].name), v)
                    print(str(v.name))
                    tree_branches.append(e1)
                    tree_branches.append(e2)
            
            #If we are already down to only 2 merged subgraphs, we can also end the cycle here 
            #under certain conditions:
            pairs = []
            if len(tmp) == 2 and hold_last == None:
                pairs.append([tmp[0], tmp[1]])
                break
            elif len(tmp) == 1 and hold_last !=None:
                pairs.append([tmp[0], hold_last])
                hold_last =None
                break
            
            #The following handles the situation of an uneven number of inputs - the remainder gets prioritized 
            #and aligned with one of the already induced subgraphs
            elif hold_last != None:
                m = 9999
                for n in range(0, len(tmp)):
                    hold_similarity = score_similarity(tmp[n], hold_last)
                    #print(str(hold_similarity))
                    if  hold_similarity < m:
                            m = hold_similarity
                            m_hold_index = n
                
                tmp_tmp = tmp[m_hold_index]
                tmp[m_hold_index] = call_subgraph_algorithm(tmp[m_hold_index], hold_last, self.supergraph)
                if construct_tree == True:
                    v = Vertex(str(tmp[m_hold_index].name))
                    tree_nodes.append(v)
                    vertex_dict.update({v.name: v})
                    e1 = Edge(vertex_dict.get(hold_last.name), v)
                    e2 = Edge(vertex_dict.get(tmp_tmp.name), v)
                    tree_branches.append(e1)
                    tree_branches.append(e2)
                tmp_tmp = None
                hold_last = None
            
            
            #Basically we have to find the next two best pairs and repeat this ad infinium until our tree is done
            for n in range(0, len(tmp)-1):
                m_hold = None
                m = 9999
                b_index = 0
                for b in range(n+1, len(tmp)):
                    if tmp[b] != None:
                        hold_similarity = score_similarity(tmp[n], tmp[b])
                        if  hold_similarity < m:
                            m = hold_similarity
                            m_hold = tmp[b]
                            b_index = b
                            
                if m_hold != None:
                    pairs.append([tmp[n], m_hold])
                    tmp[n] = None
                    tmp[b_index] = None
                
            if (not None) in tmp:
                for v in tmp:
                    if v != None:
                        hold_last = v
            
            l = len(pairs)
        
        #The result variable contains the maximum subgraph accoding to the heuristics of the
        #progressive alignment
        self.result = call_subgraph_algorithm(pairs[0][0], pairs[0][1], self.supergraph)
        if construct_tree == True:
            v = Vertex(str(self.result.name))
            tree_nodes.append(v)
            vertex_dict.update({v.name: v})
            e1 = Edge(vertex_dict.get(pairs[0][0].name), v)
            e2 = Edge(vertex_dict.get(pairs[0][1].name), v)
            tree_branches.append(e1)
            tree_branches.append(e2)
            self.tree_structure = Graph(tree_nodes, tree_branches)
            
        self.newick = str(self.result.name)
        print("Resulting tree:" + self.newick)
        #-------------------------------------------------
    
    #The following section is incomplete, as there is currently no working way to parse this mess
    #into Newick format.    
        

    
def create_tree(graph_list, draw_tree = True, name = None, supergraph = True):
    return guide_tree(graph_list, draw_tree, name, supergraph)

def traverse_tree(tree, graph_list, supergraph = True):
    graph_dict = {}
    hold = []
    for n in range(0, len(graph_list)):
        graph_dict.update({graph_list[n].name: graph_list[n]})
        
    for i in range(0, len(tree.tree_structure.vertices)):
        hold = []
        if ',' in tree.tree_structure.vertices[i].name:
            #print(str(tree.tree_structure.vertices[i].name))
            for e in tree.tree_structure.edges:
                #print(str(e.vertex_a.name))
                #print(str(e.vertex_b.name))
                if (e.vertex_b.name == tree.tree_structure.vertices[i].name and len(e.vertex_a.name) < len(tree.tree_structure.vertices[i].name)) or \
                (e.vertex_a.name == tree.tree_structure.vertices[i].name and len(e.vertex_b.name) < len(tree.tree_structure.vertices[i].name)):
                    hold.append(graph_dict.get(e.vertex_a.name))
                    
            g_add = call_subgraph_algorithm(hold[0], hold[1], supergraph)
            graph_list.append(g_add)
            graph_dict.update({g_add.name: g_add})
    
    #If the tree was created in a structured manner, the last created subgraph should be the final one - but to be safe, we organize them, by length of 
    #their identifier.
    hold = graph_list[0]
    for n in range(0, len(graph_list)):
        if len(graph_list[n].name) > len(hold.name):
            hold = graph_list[n]
    return hold

#The following function just aligns given list of preordered graphs in linear fashion.
def traverse_linear(ordered_graphs, supergraph = True):
        
    tmp = ordered_graphs[0]
    for n in range(1, len(ordered_graphs)):
        tmp = guide_tree.call_subgraph_algorithm(tmp, ordered_graphs[n], supergraph)
        
    return tmp
        