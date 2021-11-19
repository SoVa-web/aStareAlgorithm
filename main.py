from graph import Graph
from astare import Astare

if __name__ == "__main__":
    graph = Graph()
    print(Astare(graph.matrix_adjacency, graph.numberNodes, 3, 11).algorithm())