import random 
from Graph import GraphNode, Graph 

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

def main() -> None:
    maze = createRandomUnweightedGraphIter(10)
    search = GraphSearch(maze)

    traversal = []
    print("Dest: " + str(maze.nodes[9].data))
    traversal = search.DFSRec(maze.nodes[0], maze.nodes[9])
    print(traversal)

    #for node in traversal:
    #    print(node.data)

if __name__=="__main__":
    main()