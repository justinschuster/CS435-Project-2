# CS 435 Project 2 Part 2
# Author: Justin Schuster
# sorting.py 

from DirectedGraph import DirectedGraph

class TopSort:
    @staticmethod
    def Kahns(graph: DirectedGraph):
        output = []
        queue = []

        for node in graph.getAllNodes():
            if node.inDegree is 0:
                queue.append(node)

        while len(queue) is not 0:
            currNode = queue.pop(0)
            output.append(currNode)

            for neighbor in graph.adjList[currNode]:
                neighbor.inDegree = neighbor.inDegree - 1

                if neighbor.inDegree is 0:
                    queue.append(neighbor)

            currNode.inDegree = -1

        return output

    @staticmethod
    def DFSHelper(node, stack, visited, graph):
        visited.append(node)

        for neighbor in graph.adjList[node]:
            if neighbor not in visited:
                TopSort.DFSHelper(neighbor, stack, visited, graph)
                
        stack.append(node)

    # valid topological sort of the graph using mDFS algorithm 
    @staticmethod
    def mDFS(graph: DirectedGraph) -> list():
        stack = []
        visited = [] 

        for node in graph.getAllNodes():
            if node not in visited:
                TopSort.DFSHelper(node, stack, visited, graph)

        output = [] 
        while (len(stack) > 0):
            output.append(stack.pop())
        return output 