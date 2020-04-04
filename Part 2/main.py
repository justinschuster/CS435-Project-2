# CS 435 Project 2 Part 2
# Author: Justin Schuster
# main.py 

from DirectedGraph import DirectedGraph

def main() -> None:
    maze = DirectedGraph()
    maze.addNode(1)
    maze.addNode(2)

    maze.addDirectedEdge(1, 2)
    maze.removeDirectedEdge(1, 2)

    for node in maze.getAllNodes():
        print(node)

if __name__=="__main__":
    main()