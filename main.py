from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *
from Cordella_max import Cordella


def main():

    # g1 = parse("./Graphen/scriptG1.graph")
    # g2 = parse("./Graphen/cordellaTest1.graph")
    g1 = parse('./Graphen/label1.graph')
    g2 = parse('./Graphen/label2.graph')

    anker = ['1;8']
    mcis = find_mcis(g1, g2, checklabels=True)
    show_graph_comparable(g1, g2, mcis)
    # Cordella(g1, g2)
    # show_two_graphs(g1, g2)








main()
