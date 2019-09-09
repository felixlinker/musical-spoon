from modular_product import modular_product
from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *
from Cordella_max import Cordella


def main():

    g1 = parse("Graphen\graph6.graph")
    g = parse("Graphen\graph5.graph")
    # g1 = random_chess_graph(50, 50, 0)
    # g = random_chess_graph(20, 20, 0)
    
    #reverse_parser(g)
    #find_cliques(g)
    # show_graph(g1)
    # show_graph(g)
    Cordella(g, g1)






main()
