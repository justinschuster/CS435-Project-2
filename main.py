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

    # Adds a new node to the graph
    def addNode(nodeVal: GraphNode) -> None:
        return

    # adds an undirected edge between first and second (and vice versa)
    def addUndirectedEdge(first: GraphNode, second: GraphNode) -> None:
        return

    # removes an undirected edge between first and second (and vice versa)
    def removeUndirectedEdge(first: GraphNode, second: GraphNode) -> None:
        return
    
    # returns a set of all Nodes in the graph
    def getAllNodes():
        return 

def main():
    print("Hello World")
    return

if __name__=="__main__":
    main()