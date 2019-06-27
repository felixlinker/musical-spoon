from modular_product import modular_product
from parser import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *


def main():

    find_cliques('Graphen/test.graph')
    g = parse('Graphen/test.graph')
    reverse_parser(g)



main()
