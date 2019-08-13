from vertex import Vertex

class Edge:
    '''
    Edges are represented as objects
    '''
    #In this setup edges are initially treated as directed
    def __init__(self, vertex_a=Vertex, vertex_b=Vertex, label=None, weight=None):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.vertex_a.successors.append(vertex_b.name)
        self.vertex_b.predecessors.append(vertex_a.name)
        self.label = label
        self.weight = weight

    def set_weight(self, weight):
        self.weight = weight

    def set_label(self, label):
        self.label = label

    def getlabel(self):
        return self.label

    def __str__(self):
        return '(vertex_a: %s, vertex_b: %s, label: %s, weight: %s)' % (self.vertex_a, self.vertex_b, self.label, self.weight)
