import random
import timeit
from parser2 import parse
from graph import *
from edge import  *
from vertex import *

longest_vlist = 0

# TODO Abbruchbedingung bei zirkulären Graphen

def print_vertex_list(v_list):
    global longest_vlist
    if len(v_list) > longest_vlist:    # TODO wie geht man mit mehreren gleich langen Listen um
        longest_vlist = len(v_list)

    print('Clique found!: ', end='')
    for v in range(0, (len(v_list))):
        print(v_list[v], end='')
    print('\n')

def build_graph_outof_vlist(vlist):
    new_graph = Graph()
    for v in vlist:
        new_graph.add_vertex(v)
    for v in vlist:
        for s in v.successors:
            if s in new_graph.vertices:
                new_graph.add_edges(Edge(v, s))
        for s in v.predecessors:
            if s in new_graph.vertices and Edge(v, s) not in new_graph:     # 2nd condition prevents doubled edges TODO: wirklich nötig? was ist bei gerichteten Graphen?
                new_graph.add_edges(Edge(s, v))
    #TODO no_of_vertices, no_of_edges, etc nötig?
    return new_graph


# function determines the neighbors of a given vertex
def neighbors(vertex):
    neighbor_list = []
    for edge in graph.edges:
        if edge.vertex_a is vertex:
            neighbor_list.append(edge.vertex_b)
        elif edge.vertex_b is vertex:
            neighbor_list.append(edge.vertex_a)
    return neighbor_list

def find_pred_or_succ(vertex):
    neighbor_list = []
    for i in range(0, len(vertex.predecessors)):
        if vertex.predecessors[i] not in neighbor_list or vertex.predecessors[i] != vertex:
            neighbor_list.append(vertex.predecessors[i])
    for i in range(0, len(vertex.successors)):
        if vertex.successors[i] not in neighbor_list or vertex.successors[i] != vertex:
            neighbor_list.append(vertex.successors[i])
    # for v in range(0, len(neighbor_list)):
    #     print(neighbor_list[v], ' hat fogende Successors:')
    #     for x in range(0, len(neighbor_list[v].successors)):
    #         print(neighbor_list[v].successors[x])
    #     print('und folgende Predecessors:')
    #     for x in range(0, len(neighbor_list[v].predecessors)):
    #         print(neighbor_list[v].predecessors[x])
    print('Returning neighbour_list')
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


def find_cliques(graphobject):
    global graph
    graph = graphobject
    bronk([], graph.vertices, [])







