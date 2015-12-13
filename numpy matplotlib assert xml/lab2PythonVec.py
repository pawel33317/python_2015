class Node:
    id = -1
    neighbors = []
    def __init__(self, id):
        self.id = id
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
    def __str__(self):
        temp = [str(i.id) for i in self.neighbors]
        return " ".join(temp)


nodes = [Node(x) for x in xrange(8)]

nodes[0].setNeighbors([nodes[1], nodes[4]])
nodes[1].setNeighbors([nodes[0], nodes[4]])
nodes[2].setNeighbors([nodes[3], nodes[5], nodes[6]])
nodes[3].setNeighbors([nodes[2], nodes[6], nodes[7]])
      
print nodes[3]  
