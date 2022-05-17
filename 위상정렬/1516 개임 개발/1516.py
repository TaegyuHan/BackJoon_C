"""
    Solution code for "BaekJoon 개임 개발".

    - Problem link: https://www.acmicpc.net/problem/1516
"""

from sys import stdin as input
from collections import deque


class S:
    """  """
    WEIGHT_INDEX = 0


class D:
    """ Data """
    EDGE: int
    DP_WEIGHT = []
    TS_WEIGHT = []
    TS_COUNT = []
    GRAPH = []


class P:

    def __init__(self) -> None:
        D.NODE = int(input.readline())
        self._init_graph()

    def _init_graph(self):
        """ 그래프 데이터 받기 """
        for _ in range(D.NODE):
            D.DP_WEIGHT.append(0)
            D.TS_WEIGHT.append(0)
            D.TS_COUNT.append(0)
            D.GRAPH.append([])

        for end_node in range(D.NODE):
            *info, end = map(int, input.readline().split())

            if len(info) == 1:
                D.TS_WEIGHT[end_node] = info[S.WEIGHT_INDEX]
                continue

            for start_snode in info[1:]:
                D.TS_WEIGHT[end_node] = info[S.WEIGHT_INDEX]
                start_snode -= 1
                D.GRAPH[start_snode].append(end_node)
                D.TS_COUNT[end_node] += 1

    def _ts(self):
        """ 위상정렬 """

        # zero 건물 얻기
        zero_nodes = []
        for node, in_cont in enumerate(D.TS_COUNT):
            if in_cont != 0: continue
            D.DP_WEIGHT[node] = D.TS_WEIGHT[node]
            zero_nodes.append(node)

        # zero 제거
        for node in zero_nodes:
            d = deque([node])

            while d:
                cnode = d.popleft()

                for nnode in D.GRAPH[cnode]:
                    D.TS_COUNT[nnode] -= 1
                    D.DP_WEIGHT[nnode] = max(
                        D.DP_WEIGHT[nnode],
                        D.TS_WEIGHT[nnode] + D.DP_WEIGHT[cnode]
                    )
                    if D.TS_COUNT[nnode] != 0: continue
                    d.append(nnode)

    def run(self) -> None:
        self._ts()
        for weight in D.DP_WEIGHT:
            print(weight)


if __name__ == '__main__':
    # input = open('./1516.txt')
    P = P()
    P.run()