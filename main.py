from core import *
import numpy as np
import timeit




def main():

    number_of_graphs = 10
    number_of_nodes = 9
    deletion_chance = 0.1

    while np.sqrt(number_of_nodes) % 1 != 0:
        number_of_nodes += 1

    print('number of nodes:', number_of_nodes, 'with deletion chance:', deletion_chance)

    graphs = dict()
    for i in range(0, number_of_graphs):
        graphs[i] = random_chess_graph(number_of_nodes, deletion_chance, name='g'+str(i))


    tests = int(((len(graphs)-1)*(len(graphs)))/2) # gaussche summenformel um anzahl der tests zu berechnen
    c = 1

    start = timeit.default_timer()
    for i in range(0, len(graphs)):
        for j in range(i+1, len(graphs)):
            print('Testing ', graphs[i].name, 'against', graphs[j].name, '(', c, '/', tests, ')')
            c += 1
            # find_mcis_without_prompt(graphs[i], graphs[j])
            Cordella(graphs[i], graphs[j])

    stop = timeit.default_timer()
    print('time: ', stop - start)

# 10 Graphen ALL VS ALL
#             4knoten/0.1del            9knoten/0.1del
# bronk             0.1 s                   1079 s (18min)
# cordella






main()
