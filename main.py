from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *
from Cordella_max import Cordella


def main():

    g1 = parse("./Graphen/scriptG1.graph")
    g2 = parse("./Graphen/scriptG2.graph")
    # show_two_graphs(g1, g2)

    anker = ['10;4']
    mcis = find_ankered_mcis(g1, g2, anker)
    show_graph_comparable(g1, g2, mcis)









main()
