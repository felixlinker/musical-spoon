from core import *
import numpy as np
import timeit




def main():

    g9 = parse("./Graphen/scriptG1.graph")
    g10 = parse("./Graphen/cordellaTest1.graph")
   # show_two_graphs(g9, g10)
    gc = Cordella(g9, g10)
    show_graph(gc)






main()
