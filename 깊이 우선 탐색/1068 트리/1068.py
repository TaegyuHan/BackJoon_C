"""
    Solution code for "BaekJoon 트리".

    - Problem link: https://www.acmicpc.net/problem/1068
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
input = open('./1068.txt')


class D:
    """ 데이터 """
    NODE_COUNT = int(input.readline())
    NODES = list(map(int, input.readline().split()))
    CUT_NODE = int(input.readline())
    leaf_count = []
    GRAPH = {}
    ROOT_NODE = 0

    @staticmethod
    def make_graph():
        """ 그래프 생성하기 """
        for node in range(D.NODE_COUNT):
            D.leaf_count.append(0)
            D.GRAPH[node] = []

        for node1, node2 in enumerate(D.NODES):
            if node2 == -1: # 루트 노드 찾기
                D.ROOT_NODE = node1
                continue
            D.GRAPH[node2].append(node1)


class P:
    """ 문제 풀이 """

    def _DFS(self, node):
        """ 우선 깊이 탐색 """
        if not D.GRAPH[node]:
            D.leaf_count[node] = 1
            return D.leaf_count[node]

        for nnode in D.GRAPH[node]:
            D.leaf_count[node] += self._DFS(nnode)

        return D.leaf_count[node]

    def run(self) -> None:
        D.make_graph()
        self._DFS(D.ROOT_NODE)
        print(D.leaf_count[D.ROOT_NODE]
              - D.leaf_count[D.CUT_NODE])


if __name__ == '__main__':
    P = P()
    P.run()