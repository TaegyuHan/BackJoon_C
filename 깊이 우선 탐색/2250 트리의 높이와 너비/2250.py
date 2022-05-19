"""
    Solution code for "BaekJoon 트리의 높이와 너비".

    - Problem link: https://www.acmicpc.net/problem/2250
"""
from sys import stdin as input
import sys;


sys.setrecursionlimit(2500)
# input = open('./2250.txt')


class D:
    """ 데이터 """
    NODE_COUNT = int(input.readline())

    GRAPH = {}
    NODE_END = -1
    COL = 1
    node_width = {}
    nodes_count = []

    @staticmethod
    def INPUT_GRAPH():
        D.nodes_count = [0] * (D.NODE_COUNT + 1)
        """ 그래프 데이터 받기 """
        for _ in range(D.NODE_COUNT):
            node, left, right = map(int, input.readline().split())
            if node != D.NODE_END: D.nodes_count[node] += 1
            if left != D.NODE_END: D.nodes_count[left] += 1
            if right != D.NODE_END: D.nodes_count[right] += 1
            D.GRAPH[node] = (left, right)

    @staticmethod
    def FIND_ROOT_NODE():
        """ 루트 노드 찾기 """
        for node in range(1, D.NODE_COUNT + 1):
            if D.nodes_count[node] == 1:
                return node


class P:

    def _DFS(self, node, deep):
        """ 우선 깊이 탐색 """
        left, right = D.GRAPH[node]

        if left != D.NODE_END:  # 왼쪽 노드
            self._DFS(left, deep + 1)

        if deep not in D.node_width:
            D.node_width[deep] = [D.COL]  # deep 왼쪽 끝 노드
            D.COL += 1

        else:  # deep 오른쪽 노드
            if len(D.node_width[deep]) == 1:  # 오른쪽 노드 첫번째 진입
                D.node_width[deep].append(D.COL)
            else:
                D.node_width[deep][1] = D.COL
            D.COL += 1

        if right != D.NODE_END:  # 오른쪽 노드
            self._DFS(right, deep + 1)

    def _largest_width(self):
        """ 가장 긴 너비 찾기  """
        answer = (1, 1)
        maximum = 0
        for deep, width in sorted(D.node_width.items(), key=lambda x: x[0]):
            if len(width) == 1:
                if maximum != 0: continue
                answer = (deep, maximum + 1)
                maximum += 1
                continue
            if (diff := width[1] - width[0]) > maximum:
                maximum = diff
                answer = (deep, maximum + 1)
        print(*answer)

    def run(self) -> None:
        D.INPUT_GRAPH()
        self._DFS(node=D.FIND_ROOT_NODE(), deep=1)
        self._largest_width()


if __name__ == '__main__':
    P = P()
    P.run()