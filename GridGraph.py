class GridNode():
    def __init__(self, xCord, yCord, nodeVal):
        self.xCord = xCord
        self.yCord = yCord
        self.nodeVal = nodeVal
        self.edges = []

class GridGraph:
    def __init__(self, gridSize):
        self.adjMatrix = []

        for i in range(0, gridSize):
            column = []
            for j in range(0, gridSize):
                column.append(0)
            self.adjMatrix.append(column)

    # adds a node to the GridGraph
    def addGridNode(self, x, y, nodeVal):
        newNode = GridNode(x, y, nodeVal)
        self.adjMatrix[x][y] = newNode

    # adds an undirected edge to the graph
    def addUndirectedEdge(self, first, second):
        if first is not second:
            first.edges.append(second)
            second.edges.append(first)

    # removes edge from graph
    def removeUndirectedEdge(self, first, second):
        if first is not second:
            first.edges.remove(second)
            second.edges.remove(first)

    # gets all nodes in the graph 
    def getAllNodes(self):
        nodes = []
        for row in self.adjMatrix:
            for node in row:
                if node is not 0:
                    nodes.append(node)
        return nodes
