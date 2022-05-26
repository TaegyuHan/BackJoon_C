"""
    Solution code for "BaekJoon 집합의 표현".

    - Problem link: https://www.acmicpc.net/problem/1717
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(10**5)
# input = open('./1717.txt')


class D:
    """ 데이터 """
    NODE_COUNT = 0
    EDGE_COUNT = 0
    nodes = []

    UNION = 0
    FIND = 1


class P:

    def __init__(self) -> None:
        D.NODE_COUNT, D.EDGE_COUNT = map(int, input.readline().split())
        D.nodes = [i for i in range(D.NODE_COUNT + 1)]

    def _union(self, node1, node2):
        """ 합집합 """
        parent_node1 = self._find(node1)
        parent_node2 = self._find(node2)

        if parent_node1 > parent_node2:
            D.nodes[parent_node1] = parent_node2
        else:
            D.nodes[parent_node2] = parent_node1


    def _find(self, node):
        """ root 노드 찾기 """
        if D.nodes[node] == node:
            return node

        parent_node = self._find(D.nodes[node])
        D.nodes[node] = parent_node
        return parent_node

    def run(self) -> None:
        for _ in range(D.EDGE_COUNT):
            cmd, node1, node2 = map(int, input.readline().split())
            if cmd == D.UNION:
                self._union(node1, node2)
                continue

            if self._find(node1) == self._find(node2):
                print("YES")
            else:
                print("NO")


if __name__ == '__main__':
    P = P()
    P.run()