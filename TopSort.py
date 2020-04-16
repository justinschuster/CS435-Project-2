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

        # output all nodes in Q in order 
        return output

    @staticmethod
    def DFSHelper(node, stack, visited, graph):
        # set v as visited
        visited.append(node)

        # for each neighbor <- v's neighbor 
        for neighbor in graph.adjList[node]:
            # if neighbor is not visited 
            if neighbor not in visited:
                # call DFSHelper(neighbor)
                TopSort.DFSHelper(neighbor, stack, visited, graph)
                
        #append V to S
        stack.append(node)

    # valid topological sort of the graph using mDFS algorithm 
    @staticmethod
    def mDFS(graph: DirectedGraph) -> list():
        output = []

        # S is a stack
        stack = []
        visited = [] # maybe better way to do this

        # for each vertex v (node) in G
        for node in graph.getAllNodes():
            # if v is not visited 
            if node not in visited:
                # DFShelper(v)
                TopSort.DFSHelper(node, stack, visited, graph)

        # output all nodes in S in order
        while (len(stack) > 0):
            output.append(stack.pop())
        return output 