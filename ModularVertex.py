class ModularVertex:
    def __init__(self, name, vertex1, vertex2, label=None):
        self.name = name
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.label = label

    def get_vertex1(self):
        return self.vertex1

    def getname(self):
        return self.name

    def get_vertex2(self):
        return self.vertex2

    def set_node_label(self, label):
        self.label = label

    def __str__(self):
        return '(name: %s, label: %s)' % (self.name, self.label)