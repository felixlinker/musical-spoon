import random
import timeit
from parser import parse



def print_vertex_list(v_list):
    print('Clique found!: ', end='')
    for v in range(0, (len(v_list))):
        print(v_list[v], end='')
    print('\n')


# function determines the neighbors of a given vertex
def neighbors(vertex):
    neighbor_list = []
    for edge in graph.edges:
        if edge.vertex_a is vertex:
            neighbor_list.append(edge.vertex_b)
        elif edge.vertex_b is vertex:
            neighbor_list.append(edge.vertex_a)
    return neighbor_list


def count_and_sort(p, x):  # counts number of neighbors for each vertex and sorts
    w = p + x
    q = []
    for vertex in w:
        c = 0  # count variable for each vertex
        for i in range(0, len(graph.edges)):
            if graph.edges[i].vertex_a == vertex or graph.edges[i].vertex_b == vertex:
                c += 1
        q.append((vertex, c))
    j = sorted(q, key=lambda count_no: count_no[1])  # sorts List produced by count for count.number
    return j


def find_pivot(p, x):
    j = count_and_sort(p, x)
    p_with_pivot = p
    if len(j) > 0:
        pivot_vertex = j[len(j) - 1][0] # because j still consists of tuples we need [0]
        p_with_pivot = [val for val in p if val not in neighbors(pivot_vertex)]  # P\N(pivot)
    return p_with_pivot


def find_pivot_randomly(p, x):
    p_with_pivot = p
    pivot_list = p, x
    if len(pivot_list) > 0:
        pivot_vertex = random.randrange(len(pivot_list))
        p_with_pivot = [val for val in p if val not in neighbors(pivot_vertex)]  # P\N(pivot)
    return p_with_pivot


# the Bron-Kerbosch recursive algorithm
def bronk(r, p, x):
    # p_with_pivot = find_pivot(p, x)
    p_with_pivot = find_pivot_randomly(p, x)
    if len(p) == 0 and len(x) == 0:
        print_vertex_list(r)
        return
    for vertex in p_with_pivot[:]:
        r_new = r[:]
        r_new.append(vertex)
        p_new = [val for val in p if val in neighbors(vertex)]  # p intersects neighbor(vertex)
        x_new = [val for val in x if val in neighbors(vertex)]  # x intersects neighbor(vertex)
        bronk(r_new, p_new, x_new)
        p.remove(vertex)
        x.append(vertex)

#
# start = timeit.default_timer()
# bronk([], graph.vertices, [])  # without pivot: 0.0001477
# stop = timeit.default_timer()
# print('time: ', stop - start)


def find_cliques(filename):
    global graph
    graph = parse(filename)
    bronk([], graph.vertices, [])







