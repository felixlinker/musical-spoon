class Vertex:
    '''
    Vertices are represented as objects
    '''
    def __init__(self, name, label=None):
        self.name = name
        self.label = label

    def set_node_label(self, label):
        self.label = label

    def __str__(self):
        return '(name: %s, label: %s)' % (self.name, self.label)