from graph import Graph

import sys

class Astare:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.shortestDist = []
        self.numberNodes = graph.numberNodes
        self.f = 0
        self.h = 0
        self.g = 0

    def initStartDist(self):
        for i in range(self.numberNodes):
            self.shortestDist.append(sys.maxsize)


    """greedy search for the first match, if such a path does not exist, then the sum of all the weights of the graph"""
    def calcHeuristics(self, start, target):
        heuristics = 0
        visited = [False for x in range(self.numberNodes)]
        current = start
        open = [start]
        path = []
        visited[start] = True
        while len(open) != 0 and current != target:
            open = []
            for i in range(self.numberNodes):
                if self.graph[current][i] > 0:
                    open.append(i)
            minNext = self.min(open) #vertex number which one is closest
            heuristics += self.graph[current][minNext]
            current = minNext
            visited[current]
            path.append(minNext)
        if heuristics == 0:
            for i in range(self.numberNodes):
                for j in range(self.numberNodes):
                    heuristics += self.graph[i][j]
            heuristics = heuristics//2
        return heuristics

    def min(self):
        pass


    def algorithm(self):
        self.initStartDist()
        print(self.graph.matrix_adjacency)