"""
    Solution code for "BaekJoon 문제집".

    - Problem link: https://www.acmicpc.net/problem/1766
"""

from sys import stdin as input
import heapq


class D:
    """ Data """
    NODE: int
    EDGE: int
    ENTRY_ORDER = []
    ENTRY_ORDER_CHCEK = []
    GRAPH = []
    ANSWER = []


class P:

    def __init__(self) -> None:
        D.NODE, D.EDGE = map(int, input.readline().split())
        self._init_graph()

    def _init_graph(self):
        """ 그래프 데이터 생성 """
        for i in range(D.NODE):
            D.GRAPH.append([])
            D.ENTRY_ORDER.append(0)
            D.ENTRY_ORDER_CHCEK.append(False)

        for i in range(D.EDGE):
            start, end = map(int, input.readline().split())
            D.ENTRY_ORDER[end - 1] += 1
            D.GRAPH[start - 1].append(end - 1)

    def _first_node(self):
        """ 첫번째 노드 실행 """
        queue = []
        for node, in_count in enumerate(D.ENTRY_ORDER):
            if in_count != 0: continue
            heapq.heappush(queue, (node))

        while queue:
            cnode = heapq.heappop(queue)
            D.ANSWER.append(cnode + 1)
            for nnode in D.GRAPH[cnode]:
                D.ENTRY_ORDER[nnode] -= 1
                if D.ENTRY_ORDER[nnode] == 0:
                    heapq.heappush(queue, (nnode))

    def run(self) -> None:
        """ 실행 """
        self._first_node()
        print(*D.ANSWER)

if __name__ == '__main__':
    input = open('./1766.txt')
    P = P()
    P.run()