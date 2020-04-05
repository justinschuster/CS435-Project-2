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

    # creates the edges between the nodes  
    for i in range(0, random.randint(1, n*n)):
        first = random.randint(0, n-1)
        second = random.randint(0, n-1)

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

        if newGraph.isAcyclic(first) is False:
            newGraph.removeDirectedEdge(first, second)

    return newGraph

def main() -> None:
    maze = createRandomDagIter(5)

    for node in maze.getAllNodes():
        print(node)
        print(maze.adjList[node])

    if maze.isAcyclic(0) is False:
        print("False")
    else:
        print("True")

if __name__=="__main__":
    main()