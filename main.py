from modular_product import modular_product
from parser import parse
from show_graph import show_graph


def main():
    a = parse('Graphen/modularTestA.graph')
    b = parse('Graphen/modularTestB.graph')

    mod_graph = modular_product(a, b)

    # prints edgelist of modular product
    for edge in mod_graph.edges:
        print(edge.vertex_a.name, '---', edge.vertex_b.name)

    show_graph(mod_graph)



main()
