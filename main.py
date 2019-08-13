from modular_product import modular_product
from parser2 import *
from show_graph import show_graph
from random_graph import *
from bronk_pivot import *

def main():

    g = random_graph(15, 30, 0.1)
    reverse_parser(g)
    show_graph(g)
    find_cliques(g)



main()
