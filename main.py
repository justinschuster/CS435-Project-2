import random 
from Graph import GraphNode, Graph 

class GraphSearch:
    # recursive DFS traversal of the graph
    def DFSRec(start: GraphNode, end: GraphNode) -> list():
        return 

# Creates n random nodes with randomly assigned unweighted, bidirectional edges
def createRandomUnweightedGraphIter(n: int) -> Graph:
    maze = Graph(n)

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
    maze = createLinkedList(10)

    for node in maze.adjList[3]:
        print(node.data)

if __name__=="__main__":
    main()