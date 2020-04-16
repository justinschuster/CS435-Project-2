# CS 435 Project 2 Part 2
# Author: Justin Schuster
# DirectedGraph.py 

class GraphNode():
    def __init__(self, nodeVal) -> None:
        self.value = nodeVal
        self.inDegree = 0 

class DirectedGraph():
    def __init__(self) -> None:
        self.adjList = {}
        self.nodes = []

    def addNode(self, nodeVal) -> None:
        newNode = GraphNode(nodeVal)
        self.adjList[newNode] = []
        self.nodes.append(newNode)

    def addDirectedEdge(self, first, second) -> None:
        self.adjList[first].append(second)
        second.inDegree = second.inDegree + 1

    def removeDirectedEdge(self, first, second) -> None:
        self.adjList[first].remove(second)
        second.inDegree = second.inDegree - 1 

    def getAllNodes(self) -> list():
        output = []
        for key in self.adjList.keys():
            output.append(key)
            
        return output 

    def isAcyclic(self, node, path=None) -> bool:
        if len(self.adjList[node]) is 0:
            return True

        if path is None:
                path = []
        
        for neighbor in self.adjList[node]: 
            if neighbor in path:
                return False
        
            path.append(neighbor)
            return self.isAcyclic(neighbor, path)