# CS 435 Project 2 Part 2
# Author: Justin Schuster
# DirectedGraph.py 

# Don't even know if we need to create actual nodes or just entries in adjList 
#class DAGNode():
#    def __init__(self, nodeVal: int) -> None:
#        self.nodeVal = nodeVal

class GraphNode():
    def __init__(self, nodeVal) -> None:
        self.value = nodeVal
        self.inDegree = 0 

class DirectedGraph():
    def __init__(self) -> None:
        self.adjList = {}

    # adds a new node to the graph
    def addNode(self, nodeVal) -> None:
        self.adjList[nodeVal] = [] 
       
        return None 

    # problem comes in when we are specifying which nodes are first and second 
    # we don't have node objects, may need them
    # adds a directed edge between first and second
    def addDirectedEdge(self, first, second) -> None:
        self.adjList[first].append(second)

        return None

    # removes directed edge between two nodes
    def removeDirectedEdge(self, first, second) -> None:
        self.adjList[first].remove(second)

        return None 

    # returns a set of all Nodes in the graph 
    def getAllNodes(self) -> list():
        return self.adjList.keys()

    # checks to see if graph is acyclic
    def isAcyclic(self, node, path=None) -> bool:
        # No where else to go (base case)
        if len(self.adjList[node]) is 0:
            return True

        if path is None:
                path = []
        
        # check for each neighbor 
        for neighbor in self.adjList[node]: 
            if neighbor in path:
                return False
        
            path.append(neighbor)
            return self.isAcyclic(neighbor, path)