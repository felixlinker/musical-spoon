from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *


def main():

    g1 = parse('./Graphen/test.graph')
    g2 = parse('./Graphen/test.graph')
    find_mcis(g1, g2)
    #show_graph(g)



main()
