from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *



def main():

    g1 = parse('./Graphen/gewitter.graph')
    g2 = parse('./Graphen/scriptG2.graph')
    g3 = parse('./Graphen/test.graph')
    g4 = parse('./Graphen/testalpha.graph')
    # show_graph(g1)
    # show_graph(g2)
    g = find_mcis(g3, g4)
    show_graph(g)



main()
