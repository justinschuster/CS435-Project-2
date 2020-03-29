import random 

class GraphNode:
    def __init__(self, data: int) -> None:
        self.data = data

class Graph:
    def __init__(self) -> None:
        self.nodes = list()
        self.adjList = []

    # Adds a new node to the graph
    def addNode(self, nodeVal: GraphNode) -> GraphNode:
        newNode = GraphNode(nodeVal)
        self.nodes.append(newNode)
        nodeList = []
        nodeList.append(newNode)
        self.adjList.append(nodeList)
        return newNode

    # adds an undirected edge between first and second (and vice versa)
    def addUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        for node in self.adjList:
            if node[0] == first and second not in node:
                node.append(second)
            elif node[0] == second and first not in node:
                node.append(first)

    def addDirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        self.adjList[first.data].append(second)

    # removes an undirected edge between first and second (and vice versa)
    def removeUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        for nodeList in self.adjList:
            if nodeList[0] == first:
                nodeList.remove(second)
            elif nodeList[0] == second:
                nodeList.remove(first)

    # returns a set of all Nodes in the graph
    def getAllNodes(self):
        return self.nodes

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
    maze = createLinkedList(10)

    for node in maze.adjList[3]:
        print(node.data)

if __name__=="__main__":
    main()