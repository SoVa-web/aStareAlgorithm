import random

class Graph:
    def __init__(self):
        self.matrix_adjacency = [
            [0, 1, 1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]
        ]
        self.numberNodes = 7

    