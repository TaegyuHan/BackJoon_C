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
    ROOT_NODE = []

    @staticmethod
    def make_graph():
        """ 그래프 생성하기 """
        for node in range(D.NODE_COUNT):
            D.leaf_count.append(0)
            D.GRAPH[node] = []

        for node1, node2 in enumerate(D.NODES):
            if node2 == -1: # 루트 노드 찾기
                D.ROOT_NODE.append(node1)
                continue
            D.GRAPH[node2].append(node1)


class P:
    """ 문제 풀이 """

    def _one_two_node_check(self):
        """ 노드 1개 또는 2개 체크 """
        if D.NODE_COUNT >= 3: return
        elif D.NODE_COUNT == 1: print(0)
        elif D.NODE_COUNT == 2: print(1)
        exit()

    def _DFS(self, node):
        """ 우선 깊이 탐색 """
        if not D.GRAPH[node]:
            D.leaf_count[node] = 1
            return D.leaf_count[node]

        for nnode in D.GRAPH[node]:
            D.leaf_count[node] += self._DFS(nnode)

        return D.leaf_count[node]

    def run(self) -> None:
        self._one_two_node_check()
        D.make_graph()
        leaf_sum = 0
        for root_node in D.ROOT_NODE:
            leaf_sum += self._DFS(root_node)

        if leaf_sum == 1: # 줄 예외 처리
            answer = 1
        else:
            answer = leaf_sum - D.leaf_count[D.CUT_NODE]
        print(answer)

if __name__ == '__main__':
    P = P()
    P.run()
