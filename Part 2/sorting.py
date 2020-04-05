# CS 435 Project 2 Part 2
# Author: Justin Schuster
# sorting.py 

from DirectedGraph import DirectedGraph

class TopSort:

    # does a valid topological sort using Kahn's algorithm 
    @staticmethod
    def Kahns(graph: DirectedGraph) -> list():
        # let M be a dict mapping each node to its total dependencies graph.adjList is dependency dict
        # let A be an array of nodes to be outputted
        output = []

        # let Q be a queue 
        queue = []

        # add all elements of M whose values are 0 to Q
        for node in graph.adjList.keys():
            if len(graph.adjList[node]) is 0:
                queue.append(node)

        # while Q is not empty
        while len(queue) is not 0:
            # N <-- first element in Q
            # add N to A
            # decrement the in-degrees of all dependents of N
            # decrement the in-degree of N to -1 (to avoid adding it back to Q)
            # for each neighbor <-- N's neighbors
                # if neighbor has in-degree 0
                    # add neighbor to Q
            # remove N from Q
        # output all nodes in Q in order 

        pass 