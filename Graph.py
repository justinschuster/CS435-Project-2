class GraphNode:
    def __init__(self, data: int) -> None:
        self.data = data

class Graph:
    def __init__(self) -> None:
        self.nodes = [] 
        self.adjList = {}

    # Adds a new node to the graph
    def addNode(self, nodeVal: GraphNode) -> GraphNode:
        newNode = GraphNode(nodeVal)
        self.adjList[newNode] = []
        self.nodes.append(newNode)
        return newNode 

    # adds an undirected edge between first and second (and vice versa)
    def addUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        self.adjList[first].append(second)
        self.adjlist[second].append(first)

    def addDirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        self.adjList[first.data].append(second)

    # removes an undirected edge between first and second (and vice versa)
    def removeUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        self.adjList[first].remove(second)
        self.adjList[second].remove(first)

    # returns a set of all Nodes in the graph
    def getAllNodes(self):
        return self.nodes