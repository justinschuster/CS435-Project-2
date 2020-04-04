from Graph import Graph 

# Don't even know if we need to create actual nodes or just entries in adjList 
#class DAGNode():
#    def __init__(self, nodeVal: int) -> None:
#        self.nodeVal = nodeVal

class DirectedGraph():
    def __init__(self) -> None:
        self.adjList = {}

    # adds a new node to the graph
    def addNode(self, nodeVal) -> None:
        self.adjList[nodeVal] = [] 

    # adds a directed edge between first and second
    def addDirectedEdge(first, second) -> None:
        pass

    # removes directed edge between two nodes
    def removeDirectedEdge(first, second) -> None:
        pass

    # returns a set of all Nodes in the graph 
    def getAllNodes():
        pass 
