"""
    Solution code for "BaekJoon ACM Craft".

    - Problem link: https://www.acmicpc.net/problem/1005
"""
from copy import deepcopy
from sys import stdin as input
from collections import deque

class D:
    """ Data """
    TEST_COUNT: int
    NODE: int
    EDGE: int
    END_BUILD: int
    ENTRY_ORDER = []
    ENTRY_ORDER_CHECK = []
    NODE_WEIGHT = []
    DP_WEIGHT_CHEK = []
    GRAPH = []


class P:

    def __init__(self) -> None:
        D.TEST_COUNT = int(input.readline())

    def _input_data(self):
        """ 데이터 받기 """
        D.NODE, D.EDGE = map(int, input.readline().split())
        D.NODE_WEIGHT = list(map(int, input.readline().split()))

        D.ENTRY_ORDER = []
        D.DP_WEIGHT_CHEK = []
        D.ENTRY_ORDER_CHECK = []
        D.GRAPH = []

        for _ in range(D.NODE):
            D.ENTRY_ORDER.append(0)
            D.DP_WEIGHT_CHEK.append(0)
            D.ENTRY_ORDER_CHECK.append(False)
            D.GRAPH.append([])

        # 노드 연결 저장
        for _ in range(D.EDGE):
            start, end = map(int, input.readline().split())
            D.ENTRY_ORDER[end - 1] += 1
            D.GRAPH[start - 1].append(end - 1)

        # 종료 노드
        D.END_BUILD = int(input.readline())

    def _next_node(self, first_node):
        """ 다음 노드 동작하기 """

        d = deque([first_node])
        D.DP_WEIGHT_CHEK[first_node] = \
            deepcopy(D.NODE_WEIGHT[first_node])


        while d:
            cnode = d.popleft()
            D.ENTRY_ORDER_CHECK[cnode] = True

            for nnode in D.GRAPH[cnode]:
                D.ENTRY_ORDER[nnode] -= 1
                D.DP_WEIGHT_CHEK[nnode] = max(
                    D.DP_WEIGHT_CHEK[cnode] + D.NODE_WEIGHT[nnode],
                    D.DP_WEIGHT_CHEK[nnode]
                )
                if D.ENTRY_ORDER[nnode] != 0: continue
                d.append(nnode)

    def _first_node_start(self):
        """ 첫번째 노드 시작 """
        for node, in_count in enumerate(D.ENTRY_ORDER):
            if in_count != 0: continue
            if D.ENTRY_ORDER_CHECK[node]: continue
            self._next_node(node)

    def run(self) -> None:
        for _ in range(D.TEST_COUNT):
            self._input_data()
            self._first_node_start()
            print(D.DP_WEIGHT_CHEK[D.END_BUILD - 1])


if __name__ == '__main__':
    # input = open('./1005.txt')
    P = P()
    P.run()