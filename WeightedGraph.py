# CS 435 Project 2 Part 2
# Author: Justin Schuster
# weightedgraph.py 

class WeightedGraphEdge():
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight 

class WeightedGraphNode():
    def __init__(self, nodeVal) -> None:
        self.value = nodeVal

class WeightedGraph():
    def __init__(self) -> None:
        self.adjList = {}

    # adds a node to the graph 
    def addNode(self, nodeVal) -> WeightedGraphNode:
        newNode = WeightedGraphNode(nodeVal)
        self.adjList[newNode] = []
        return newNode 

    # creates a directed weighted edge from first to second
    def addWeightedEdge(self, first, second, edgeWeight) -> None:
        newEdge = WeightedGraphEdge(second, edgeWeight)
        self.adjList[first].append(newEdge)

    # removes an edge from
    def removeWeightedEdge(self, first, second) -> None:
        for edge in self.adjList[first]:
            if edge.dest is second:
                self.adjList[first].remove(edge)

    # gets all nodes in the graph
    def getAllNodes(self) -> list():
        output = []
        for key in self.adjList.keys():
            output.append(key)
            
        return output 
