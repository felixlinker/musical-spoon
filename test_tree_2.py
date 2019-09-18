# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:40:15 2019

@author: Arctandra
"""

from vertex import Vertex
from edge import Edge
from graph import Graph
from show_graph import show_graph
from random_graph import random_graph
from random_graph import random_chess_graph
import Cordella_max
from Parser import parse
from guide_tree import guide_tree
import bronk_pivot


#g1 = parse("graph1.graph")
#g2 = parse("graph2.graph")
#g3 = parse("graph3.graph")
#g4 = parse("graph4.graph")

#Names for Graphs! Keine Sorge, außer dass es nun eine Möglichkeit der namentlichen Zuordnung gibt, ändert sich nix. Der Default bleibt None.
g1 = random_chess_graph(4, 4)
g1.name = "Graph1"
g2 = random_chess_graph(4, 4)
g2.name = "Graph2"
g3 = random_chess_graph(9, 9)
g3.name = "Graph3"
g4 = random_chess_graph(4, 4)
g4.name = "Graph4"
g5 = random_chess_graph(4, 4)
g5.name = "Graph5"

#show_graph(g1)
show_graph(g2)
show_graph(g3)
show_graph(g1)
show_graph(g4)
show_graph(g5)

t = guide_tree([g1, g3, g2, g4, g5], True)
show_graph(t.result)


show_graph(t.tree_structure)

#g3= bronk_pivot.find_mcis_without_prompt(g1, g2)


