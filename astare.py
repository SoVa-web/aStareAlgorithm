from graph import Graph

import numpy
import random
import sys

class Node:
        def __init__(self, number_node = None):
            self.node = number_node
            self.g = 0 
            self.previous = None

class Astare:
    def __init__(self, graph: Graph, numberNodes, start, target):
        self.graph = graph
        self.numberNodes = numberNodes
        self.start = Node(start)
        self.target = Node(target)
        self.path = []
        self.hueristics = [
        [0, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 3, 4, 5, 6],
        [1, 0, 1, 2, 3, 2, 1, 2, 3, 2, 3, 4, 4, 3, 4, 5],
        [2, 1, 0, 1, 2, 1, 2, 3, 4, 3, 2, 3, 5, 4, 3, 4],
        [3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 6, 5, 4, 3],
        [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 5, 4, 3, 2],
        [3, 2, 1, 2, 1, 0, 1, 2, 3, 2, 1, 2, 4, 3, 2, 3],
        [2, 1, 2, 3, 2, 1, 0, 1, 2, 1, 2, 3, 3, 2, 3, 4],
        [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 2, 3, 4, 5],
        [2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 1, 2, 3, 4],
        [3, 2, 3, 4, 3, 2, 1, 2, 1, 0, 1, 2, 2, 1, 2, 3],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 1, 0, 1, 3, 2, 1, 2],
        [5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, 4, 3, 2, 1],
        [3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 0, 1, 2, 3],
        [4, 3, 4, 5, 4, 3, 2, 3, 2, 1, 2, 3, 1, 0, 1, 2],
        [5, 4, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 2, 1, 0, 1],
        [6, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 1, 3, 2, 1, 0],
        ]
        
        """[
            [0, 1, 2, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [2, 1, 0, 1, 2, 2, 0],
            [0, 0, 1, 0, 0, 1, 1],
            [1, 0, 2, 0, 0, 1, 0],
            [0, 0, 2, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]
        ] """
        #use random:)
        """for i in range(self.numberNodes):
            self.hueristics.append(numpy.array([random.randint(1, 10) for x in range(self.numberNodes)]))
        for i in range(self.numberNodes):
            for j in range(self.numberNodes):
                self.hueristics[i][j] = self.hueristics[j][i]
                if i == j:
                    self.hueristics[i][j] = 0"""
            


    def algorithm(self): 
        open = [self.start]
        closed = []
        while open:
            current_node = self.choose_node(open)
            if current_node.node == self.target.node:
                return self.build_path(current_node, closed)
            open.remove(current_node)
            closed.append(current_node)
            new_open = self.get_adjacent_nodes(current_node, closed)
            for adjacent in new_open:
                if adjacent not in open:
                    open.append(adjacent)
                    adjacent.previous = current_node.node
                    adjacent.g = current_node.g + self.graph[current_node.node][adjacent.node]
                if current_node.g + 1  < adjacent.g: 
                    adjacent.previous = current_node.node
                    adjacent.g = current_node.g + 1
        return "Path not exist"

    def get_adjacent_nodes(self, current_node, closed):
        new_open = []
        new_open_node = []
        for adjacent in range(self.numberNodes):
            if self.graph[current_node.node][adjacent] > 0:
                new_open.append(adjacent)
        for closed_node in closed:
            if closed_node.node in new_open:
                new_open.remove(closed_node.node)
        for node in new_open:
            new_open_node.append(Node(node))
        return new_open_node


    def build_path(self, to_node, closed):
        path = []
        while to_node.previous != None:
            path.append(to_node.node)
            for node in closed:
                if to_node.previous == node.node:
                    to_node = node
        path.append(self.start.node)
        path.reverse()
        return path

    def  choose_node (self, open):
        min_cost = sys.maxsize
        best_node = None

        for node in open:
            cost_start_to_node = node.g
            cost_node_to_goal = self.hueristics[node.node][self.target.node]
            total_cost = cost_start_to_node + cost_node_to_goal

            if min_cost > total_cost:
                min_cost = total_cost
                best_node = node

        return best_node

            
        