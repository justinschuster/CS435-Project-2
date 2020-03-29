class GraphNode:
    def __init__(self, data: int) -> None:
        self.data = data

class Graph:
    def __init__(self) -> None:
        self.nodes = list()
        self.adjList = []

    # Adds a new node to the graph
    def addNode(self, nodeVal: GraphNode) -> GraphNode:
        newNode = GraphNode(nodeVal)
        self.nodes.append(newNode)
        nodeList = []
        nodeList.append(newNode)
        self.adjList.append(nodeList)
        return newNode

    # adds an undirected edge between first and second (and vice versa)
    def addUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        for node in self.adjList:
            if node[0] == first and second not in node:
                node.append(second)
            elif node[0] == second and first not in node:
                node.append(first)

    def addDirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        self.adjList[first.data].append(second)

    # removes an undirected edge between first and second (and vice versa)
    def removeUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        for nodeList in self.adjList:
            if nodeList[0] == first:
                nodeList.remove(second)
            elif nodeList[0] == second:
                nodeList.remove(first)

    # returns a set of all Nodes in the graph
    def getAllNodes(self):
        return self.nodes