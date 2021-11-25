from sys import stdin as input
from collections import deque

class AdjacencyMatrix:

    def __init__(self):
        self.matrix = []
        self.start_node = 0
        self.visited = []

    def input_data(self):
        N, M, self.start_node = map(int, input.readline().split())
        self.matrix = [[False for _ in range(N)] for _ in range(N)]

        for _ in range(M):
            node1, node2 = map(int, input.readline().split())
            self.matrix[node1 - 1][node2 - 1] = True
        return

    def DFS(self, cur_node, visited):
        visited += [self.start_node]
        for c in range(len(self.matrix[cur_node])):
            if self.matrix[self.start_node][c] == 1 and (c not in visited):
                self.DFS(c, visited)
        return visited

    def BFS(self):
        self.visited = [self.start_node]
        queue = [self.start_node]
        while queue:
            n = queue.pop(0)
            for c in range(len(self.matrix[self.start_node])):
                if self.matrix[n][c] == 1 and (c not in self.visited):
                    self.visited.append(c)
                    queue.append(c)
        return self.visited

    def result(self):
        self.DFS(AM.start_node)
        print(" ".join(map(str, self.DFS_result)))
        print(" ".join(map(str, self.BFS())))


if __name__ == "__main__":
    input = open("./1260.txt")
    AM = AdjacencyMatrix()
    AM.input_data()
    AM.result()
