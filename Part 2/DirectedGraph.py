# CS 435 Project 2 Part 2
# Author: Justin Schuster
# DirectedGraph.py 

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
        print("Added node to adjacencyy list")
        print(self.adjList[nodeVal])

        return None 

    # adds a directed edge between first and second
    def addDirectedEdge(first, second) -> None:
        pass

    # removes directed edge between two nodes
    def removeDirectedEdge(first, second) -> None:
        pass

    # returns a set of all Nodes in the graph 
    def getAllNodes():
        pass 
