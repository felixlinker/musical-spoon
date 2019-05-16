# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:07:57 2019

@author: Arctandra
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def show_graph(g):
    
    edge_list = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for e in g.edges:
        if str(e.vertex_a.name).isalpha():
            n1_pos = alphabet.find(str(e.vertex_a.name))
            n2_pos = alphabet.find(str(e.vertex_b.name))
            edge_list.append((n1_pos, n2_pos))
        
        else:
            n1_pos = int(e.vertex_a.name)
            n2_pos = int(e.vertex_b.name)
            edge_list.append((n1_pos, n2_pos))
    
    G = nx.Graph()
    G.add_edges_from(edge_list)
    nx.draw(G,with_labels=True)
    plt.show()

