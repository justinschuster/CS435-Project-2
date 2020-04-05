# CS 435 Project 2 Part 2
# Author: Justin Schuster
# sorting.py 

from DirectedGraph import DirectedGraph

class TopSort:
    # does a valid topological sort using Kahn's algorithm 
    @staticmethod
    def Kahns(graph: DirectedGraph):
        # let M be a dict mapping each node to its total dependencies graph.adjList is dependency dict
        # let A be an array of nodes to be outputted
        output = []

        # let Q be a queue 
        queue = []

        # add all elements of M whose values are 0 to Q
        for node in graph.getAllNodes():
            print("Node: %d, in degree: %d"% (node.value, node.inDegree))
            if node.inDegree is 0:
                queue.append(node)

        # while Q is not empty
        while len(queue) is not 0:
            # N <-- first element in Q
            currNode = queue.pop(0)

            # add N to A
            output.append(currNode)

            # decrement the in-degrees of all dependents of N
            for neighbor in graph.adjList[currNode]:
                neighbor.inDegree = neighbor.inDegree - 1

                if neighbor.inDegree is 0:
                    queue.append(neighbor)

            # decrement the in-degree of N to -1 (to avoid adding it back to Q)
            currNode.inDegree = -1

            # for each neighbor <-- N's neighbors
            #for neighbor in graph.adjList[currNode]:
                # if neighbor has in-degree 0
                #if neighbor.inDegree is 0:
                    # add neighbor to Q
                    #queue.append(neighbor)

            # remove N from Q
            #queue.remove(currNode)

        # output all nodes in Q in order 
        return output