from core import *
import numpy as np
import timeit




def main():

    # g1 = parse("./Graphen/scriptG1.graph")
    # g2 = parse("./Graphen/cordellaTest1.graph")
    number_of_nodes = 9
    deletion_chance = 0.1

    while np.sqrt(number_of_nodes) % 1 != 0:
        number_of_nodes += 1

    print('number of nodes:', number_of_nodes, 'with deletion chance:', deletion_chance)

    g0 = random_chess_graph(number_of_nodes, deletion_chance, name='g0')
    g1 = random_chess_graph(number_of_nodes, deletion_chance, name='g1')
    g2 = random_chess_graph(number_of_nodes, deletion_chance, name='g2')
    g3 = random_chess_graph(number_of_nodes, deletion_chance, name='g3')
    g4 = random_chess_graph(number_of_nodes, deletion_chance, name='g4')
    g5 = random_chess_graph(number_of_nodes, deletion_chance, name='g5')
    g6 = random_chess_graph(number_of_nodes, deletion_chance, name='g6')
    g7 = random_chess_graph(number_of_nodes, deletion_chance, name='g7')
    g8 = random_chess_graph(number_of_nodes, deletion_chance, name='g8')
    g9 = random_chess_graph(number_of_nodes, deletion_chance, name='g9')
    # show_graph_comparable(g1, g2, g0)
    # Cordella(g1, g2)
    # mcis = find_mcis(g1, g2, checklabels=True)

    gl = [g0, g1, g2, g3, g4, g5, g6, g7, g8, g9]
    testees = len(gl)
    tests = 0
    c = 1
    while testees-1 != 0:
        tests += testees-1
        testees += -1

    start = timeit.default_timer()
    for i in range(0, len(gl)):
        for j in range(i+1, len(gl)):
            print('Testing ', gl[i].name, 'against', gl[j].name, '(', c, '/', tests, ')')
            c += 1
            find_mcis_without_prompt(gl[i], gl[j])
            # Cordella(gl[i], gl[j])

    stop = timeit.default_timer()
    print('time: ', stop - start)

# 10 Graphen ALL VS ALL
#             4knoten/0.1del            9knoten/0.1del
# bronk             0.1 s                   1079 s (18min)
# cordella






main()
