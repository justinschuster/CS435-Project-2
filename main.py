class Edge:
    def __init__(self, dir, d=None, s=None) -> None:
        self.directed = dir 

        if self.directed is True:
            self.dest = d
            self.source = s
        else:
            self.dest = None
            self.source = None

class GraphNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.neighbors = list()

class Graph:
    def __init__(self) -> None:
        self.nodes = list()
        self.edges = list()

    # Adds a new node to the graph
    def addNode(self, nodeVal: GraphNode) -> None:
        newNode = GraphNode(nodeVal)
        self.nodes.append(newNode)
        return

    # adds an undirected edge between first and second (and vice versa)
    def addUndirectedEdge(first: GraphNode, second: GraphNode) -> None:
        return

    # removes an undirected edge between first and second (and vice versa)
    def removeUndirectedEdge(first: GraphNode, second: GraphNode) -> None:
        return
    
    # returns a set of all Nodes in the graph
    def getAllNodes(self):
        return self.nodes

def main() -> None:
    maze = Graph()
    maze.addNode(5)

    nodes = maze.getAllNodes()
    for node in nodes:
        print(node.data)
    

if __name__=="__main__":
    main()