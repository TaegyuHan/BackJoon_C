"""
    Solution code for "BaekJoon 전력난".

    - Problem link: https://www.acmicpc.net/problem/6497
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./6497.txt')


class D:
    """ 데이터 """
    NODE_COUNT = 0
    EDGE_COUNT = 0
    cost_sum = 0
    parent_nodes = {}
    edges_data = []

    @staticmethod
    def init_data():
        """ 데이터 초기화 """
        D.cost_sum = 0
        D.parent_nodes = [i for i in range(D.NODE_COUNT)]
        D.edges_data = []


class P:

    def input_check(self):
        """ 데이터 받기 체크 """
        D.NODE_COUNT, D.EDGE_COUNT = map(int, input.readline().split())
        if D.NODE_COUNT or D.EDGE_COUNT:
            return True
        return False

    def input_data(self):
        """ 데이터 받기 """
        D.init_data()

        for _ in range(D.EDGE_COUNT):
            node1, node2, weight = map(int, input.readline().split())
            D.cost_sum += weight
            D.edges_data.append((weight, node1, node2))
        D.edges_data.sort()

    def union(self, node1, node2) -> int:
        """ 합집합 """
        parent_node1 = self.find(node1)
        parent_node2 = self.find(node2)

        if parent_node1 > parent_node2:
            D.parent_nodes[parent_node1] = parent_node2
            return parent_node2
        else:
            D.parent_nodes[parent_node2] = parent_node1
            return parent_node1

    def find(self, node) -> int:
        """ 부모노드 찾기 """
        if D.parent_nodes[node] == node:
            return node

        D.parent_nodes[node] = self.find(D.parent_nodes[node])
        return D.parent_nodes[node]

    def run(self) -> None:
        while self.input_check():
            self.input_data()

            for weight, node1, node2 in D.edges_data:
                if self.find(node1) == self.find(node2):
                    continue
                self.union(node1, node2)
                D.cost_sum -= weight
            print(D.cost_sum)


if __name__ == '__main__':
    P = P()
    P.run()