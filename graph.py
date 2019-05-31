class Graph:
    '''
    Graph object consisting of vertices and edges
    '''

    def __init__(self, vertices: [] = None, edges: [] = None):
        self.vertices = vertices    # list of vertex objects
        self.edges = edges          # list of edge objects
        if vertices is None:
            self.vertices = []
        if edges is None:
            self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edges(self, edge):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    # def __str__(self):
    #     return '(vertices: %s, edges: %s)' % (self.vertices, self.edges)
