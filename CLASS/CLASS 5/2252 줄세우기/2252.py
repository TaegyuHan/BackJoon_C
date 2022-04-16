"""
    Solution code for "BaekJoon 줄 세우기".

    - Problem link: https://www.acmicpc.net/problem/2252
"""

from sys import stdin as input
from collections import deque


class D:
    """ data """
    NODE: int
    EDGE: int
    ENTRY_ORDER = []
    ENTRY_ORDER_CHECK = []
    GRAPH = []


class P:

    def __init__(self) -> None:
        D.NODE, D.EDGE = map(int, input.readline().split())
        self._init_graph()

    def _init_graph(self):
        """ 그래프 데이터 받기 """
        for _ in range(D.NODE):
            D.ENTRY_ORDER.append(0)
            D.ENTRY_ORDER_CHECK.append(False)
            D.GRAPH.append([])

        for i in range(D.EDGE):
            front, end = map(int, input.readline().split())
            D.ENTRY_ORDER[end - 1] += 1
            D.GRAPH[front - 1].append(end - 1)

    def _next_node(self, first_node):
        """ 첫번째 노드에서 다음노드로 이동하기 """
        d = deque([first_node])

        while d:
            current_node = d.popleft()
            self._answer.append(current_node + 1)

            for next_node in D.GRAPH[current_node]:
                D.ENTRY_ORDER[next_node] -= 1
                if D.ENTRY_ORDER[next_node] != 0: continue
                D.ENTRY_ORDER_CHECK[next_node] = True # 0계산 완료 됐는지 확인
                d.append(next_node)

    def _first_node(self):
        """ 위상정렬 첫번째 노드 """
        self._answer = []
        for node, in_count in enumerate(D.ENTRY_ORDER):
            if in_count != 0: continue
            if D.ENTRY_ORDER_CHECK[node]: continue
            self._next_node(node)

        print(" ".join(map(str, self._answer)))

    def run(self) -> None:
        """ 실행 """
        self._first_node()


if __name__ == '__main__':
    # input = open('./2252.txt')
    P = P()
    P.run()