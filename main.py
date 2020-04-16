import random 

from Graph import GraphNode, Graph 
from WeightedGraph import WeightedGraph
from TopSort import TopSort
from GridGraph import GridGraph
from DirectedGraph import DirectedGraph

class GraphSearch:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = [False] * len(graph.nodes)
        self.traversal = []

    # recursive DFS traversal of the graph
    def DFSRec(self, start: GraphNode, end: GraphNode) -> list():
        if (self.visited[start.data] == False):
            return self.dfsHelper(start, end) 
                
    def dfsHelper(self, current: GraphNode, end: GraphNode):
        # mark visited 
        self.visited[current.data] = True
        self.traversal.append(current)

        # "process"
        if (current.data == end.data):
            return self.traversal

        # Not sure how to add it to array right now 
        # for each vertex that has an edge from v:
        for vertex in self.graph.adjList[current.data]:
            # if v is not visited 
            if (self.visited[vertex.data] == False):
                # dfs v
                self.DFSRec(vertex, end)

# Creates n random nodes with randomly assigned unweighted, bidirectional edges
def createRandomUnweightedGraphIter(n: int) -> Graph:
    maze = Graph()

    for i in range(0, n):
        maze.addNode(i)

    numEdges = random.randint(1, n*n)
    for i in range(0, numEdges):
        firstNode = random.randint(0, n-1)
        secondNode = random.randint(0, n-1)
        if firstNode != secondNode:
            maze.addUndirectedEdge(maze.nodes[firstNode], maze.nodes[secondNode])

    return maze

# creates Graph n nodes. Each node only has an edge to the next node created
def createLinkedList(n: int) -> Graph:
    maze = Graph()

    for i in range(0, n):
        maze.addNode(i)

    for i in range(0, n-1):
        maze.addDirectedEdge(maze.nodes[i], maze.nodes[i+1])

    return maze

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
    # Directed Graph Tests 
    directedGraph = createRandomDagIter(5)

    res = TopSort.mDFS(directedGraph)
    for node in res:
        print(node.value)

if __name__=="__main__":
    main()

