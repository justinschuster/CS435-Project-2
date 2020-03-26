class UndirectedEdge:
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second
        
class GraphNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.neighbors = list()

class Graph:
    def __init__(self) -> None:
        self.nodes = list()
        self.un_edges = list()

    # Adds a new node to the graph
    def addNode(self, nodeVal: GraphNode) -> GraphNode:
        newNode = GraphNode(nodeVal)
        self.nodes.append(newNode)
        return newNode

    # adds an undirected edge between first and second (and vice versa)
    def addUndirectedEdge(self, first: GraphNode, second: GraphNode) -> None:
        newEdge = UndirectedEdge(first, second)
        self.un_edges.append(newEdge)

    # removes an undirected edge between first and second (and vice versa)
    def removeUndirectedEdge(first: GraphNode, second: GraphNode) -> None:
        return
    
    # returns a set of all Nodes in the graph
    def getAllNodes(self):
        return self.nodes

def main() -> None:
    maze = Graph()
    first = maze.addNode(5)
    second = maze.addNode(6)

    #nodes = maze.getAllNodes()
    #for node in nodes:
        #print(node.data)

    maze.addUndirectedEdge(first, second)

    for edge in maze.un_edges:
        print(edge.first.data)

    

if __name__=="__main__":
    main()