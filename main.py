from modular_product import modular_product
from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *
from cordelle_v_0_2 import Cordella


def main():

    g = random_graph(10, 10, 0)
    #g1 = random_graph(100, 100, 0)
    #reverse_parser(g)
    #show_graph(g)
    #find_cliques(g)
    Cordella(g, g)



main()
