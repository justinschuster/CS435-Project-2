class GraphNode:
    def __init__(self, data: int) -> None:
        self.data = data
        #self.edges = list()

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
            if node[0] == first:
                node.append(second)
            elif node[0] == second:
                node.append(first)

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

    return maze

def main() -> None:
    maze = Graph()
    first = maze.addNode(5)
    second = maze.addNode(6)

    #nodes = maze.getAllNodes()
    #for node in nodes:
        #print(node.data)

    maze.addUndirectedEdge(first, second)
    maze.removeUndirectedEdge(first, second)

    for node in maze.adjList:
        for neighbor in node:
            print(neighbor.data)

    
    
    
    
    
    

    

if __name__=="__main__":
    main()