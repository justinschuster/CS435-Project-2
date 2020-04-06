# CS 435 Project 2 Part 2
# Author: Justin Schuster
# main.py 

import random 

from DirectedGraph import DirectedGraph
from weightedgraph import WeightedGraph
from sorting import TopSort

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

def main() -> None:
    '''  
    maze = createRandomDagIter(10)

    for node in maze.adjList.keys():
        for neighbor in maze.adjList[node]:
            print("%d -> %d"% (node.value, neighbor.value))
        print()

    #sorted = TopSort.Kahns(maze)
    #print("\nKahns")
    #for i in sorted:
    #    print(i.value)

    TopSort.mDFS(maze)
    '''

    graphWeighted = createLinkedList(5)

    for node in graphWeighted.getAllNodes():
        for edge in graphWeighted.adjList[node]:
            print("First: %d, Second: %d, Weight: %d"% (node.value, edge.dest.value, edge.weight))

if __name__=="__main__":
    main()