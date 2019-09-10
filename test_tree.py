# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:58:35 2019

@author: Christopher
"""

from guide_tree import guide_tree
from vertex import Vertex
from edge import Edge
from graph import Graph
import random_graph
from show_graph import show_graph 

g1 = random_graph.random_graph(8, 8)
g2 = random_graph.random_graph(5, 5)
g3 = random_graph.random_graph(6, 6)
g4 = random_graph.random_graph(7, 7)

show_graph(g1)
show_graph(g2)
show_graph(g3)
show_graph(g4)

g_list = []
g_list.append(g1)
g_list.append(g2)
g_list.append(g3)
g_list.append(g4)

t = guide_tree(g_list)
print(str(len(t.result.edges))) #This all too often produces a zero graph - correct vertices but no edges.
show_graph(t.result)