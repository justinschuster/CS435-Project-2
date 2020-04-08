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
        pass

    # adds an undirected edge to the graph
    def addUndirectedEdge(self, first, second):
        pass

    # removes edge from graph
    def removesUndirectedEdge(self, first, second):
        pass

    # gets all nodes in the graph 
    def getAllNodes():
        pass