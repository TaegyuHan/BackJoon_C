from sys import stdin as input
from collections import deque

class P1240:

    def input_data(self):
        self.node_list = {}
        self.N, self.M = map(int, input.readline().split())

        for _ in range(self.N - 1):
            n1, n2, distance = input.readline().split()
            if n1 not in self.node_list.keys():
                self.node_list[n1] = set()
                self.node_list[n1].add((n2, distance))
            else:
                self.node_list[n1].add((n2, distance))

            if n2 not in self.node_list.keys():
                self.node_list[n2] = set()
                self.node_list[n2].add((n1, distance))
            else:
                self.node_list[n2].add((n1, distance))

    def result(self):
        for _ in range(self.M):
            n1, n2 = input.readline().split()
            answer = 0
            while True:
                print(self.node_list[n1])
                break

            break

if __name__ == '__main__':
    input = open("./1240.txt")
    P = P1240()
    P.input_data()
    P.result()