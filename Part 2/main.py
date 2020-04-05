# CS 435 Project 2 Part 2
# Author: Justin Schuster
# main.py 

import random 

from DirectedGraph import DirectedGraph

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

def main() -> None:
    maze = createRandomDagIter(10)

    #for node in maze.adjList.keys():
    #    print()
    #    for neighbor in maze.adjList[node]:
    #        print("%d -> %d"% (node.value, neighbor.value))

if __name__=="__main__":
    main()