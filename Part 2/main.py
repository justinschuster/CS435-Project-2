# CS 435 Project 2 Part 2
# Author: Justin Schuster
# main.py 

import random 

from DirectedGraph import DirectedGraph
from weightedgraph import WeightedGraph
from sorting import TopSort
from gridgraph import GridGraph

# iteratively creates a DAG with n nodes
# need to create an isValid check after we create a node 
# should check to see if the new edge has cause the graph to be cyclical 
def createRandomDagIter(n: int) -> DirectedGraph:
    newGraph = DirectedGraph()

    # creates n nodes for the graph
    for i in range(0, n):
        newGraph.addNode(i)

    nodes = newGraph.getAllNodes()
    
    # creates the edges between the nodes  
    for i in range(0, random.randint(1, n*n)):
        first = nodes[random.randint(0, n-1)]
        second = nodes[random.randint(0, n-1)]

        # can't connect to itself 
        if (first == second):
            continue
        
        # can't traverse backwards 
        if second in newGraph.adjList[first] or first in newGraph.adjList[second]:
            continue

        # can only traverse forward or right meaning 2 edges max
        if (len(newGraph.adjList[first]) == 2):
            continue
        
        #print("First: %d, Second: %d"% (first, second))
        newGraph.addDirectedEdge(first, second)
        #print("New edge: %d -> %d"% (first.value, second.value))

        if newGraph.isAcyclic(first) is False:
            #print("Removed")
            newGraph.removeDirectedEdge(first, second)

    return newGraph

# creates a Complete weighted graph with n nodes
# each node has random integer weighted edge to every other node 
# n(n-1) total edges 
def createRandomCompleteWeightedGraph(n: int) -> WeightedGraph:
    graph = WeightedGraph()

    for i in range(0, n):
        graph.addNode(i)

    for node in graph.getAllNodes():
        for neighbor in graph.getAllNodes():
            if node is not neighbor:
                weight = random.randint(0, n)
                graph.addWeightedEdge(node, neighbor, weight)

    return graph 

# weighted graph with n nodes each with a single edge to the next node
def createLinkedList(n: int) -> WeightedGraph:
    graph = WeightedGraph()

    prevNode = None 
    for i in range(0, n):
        newNode = graph.addNode(i)

        if prevNode is not None:
            graph.addWeightedEdge(prevNode, newNode, 1)

        prevNode = newNode 
    
    return graph 

# creates n by n GridGraph
# 50% chances nodes are connected to its neighbors
# 0% chance for non-neighbors 
def createRandomGridGraph(n):
    graph = GridGraph(n)

    nodeCount = 0
    for x in range(0, n):
        for y in range(0, n):
            graph.addGridNode(x, y, nodeCount)
            
            if x is not 0:
                if random.randint(0, 1) is 1:
                   graph.addUndirectedEdge(graph.adjMatrix[x][y], graph.adjMatrix[x-1][y]) 

            if y is not 0:
                if random.randint(0, 1) is 1:
                    graph.addUndirectedEdge(graph.adjMatrix[x][y], graph.adjMatrix[x][y-1]) 

            nodeCount += 1

    return graph 

# returns a dictionary mapping each node in the graph
# to the minimum value from start to get to each node 
def dijkstras(start):
    pass

def main() -> None:
    '''
    graphWeighted = createLinkedList(5)

    for node in graphWeighted.getAllNodes():
        for edge in graphWeighted.adjList[node]:
            print("First: %d, Second: %d, Weight: %d"% (node.value, edge.dest.value, edge.weight))
    '''

    graphGrid = createRandomGridGraph(5)
'''
    for i in range(0,5):
        for j in range(0,5):
            node = graphGrid.adjMatrix[i][j]
            for edge in node.edges:
                print("Node: %d,%d, neighbor: %d,%d"% (node.xCord, node.yCord, edge.xCord, edge.yCord))
'''

if __name__=="__main__":
    main()