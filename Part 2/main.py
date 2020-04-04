# CS 435 Project 2 Part 2
# Author: Justin Schuster
# main.py 

from DirectedGraph import DirectedGraph

# iteratively creates a DAG with n nodes
def createRandomDagIter(n: int) -> DirectedGraph:
    newGraph = DirectedGraph()

    for i in range(0, n):
        newGraph.addNode(i)

    return newGraph

def main() -> None:
    maze = createRandomDagIter(5)

    for node in maze.getAllNodes():
        print(node)

if __name__=="__main__":
    main()