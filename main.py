from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *
from Cordella_max import *



def main():

    g1 = parse('./Graphen/graph8.graph')
    g2 = parse('./Graphen/graph6.graph')
    g3 = parse('./Graphen/test.graph')
    g4 = parse('./Graphen/testalpha.graph')
    #show_graph(g1)
    #show_graph(g2)
    #g = Cordella(g3, g4)
    gx = find_mcis(g1, g2)
    #show_graph_comparable(g3, g4, gx)# TODO show_graph für cordella?


main()
