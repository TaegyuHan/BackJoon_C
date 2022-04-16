"""
    Solution code for "BaekJoon 최소비용 구하기".

    - Problem link: https://www.acmicpc.net/problem/1916
"""

from sys import stdin as input
from sys import maxsize as InF
import heapq


class D:
    """ Data """
    NDOE: int
    EDGE: int
    GRAPH = []

    # 도시
    START: int
    END: int

    # 정답
    PATH = []


class P:

    def __init__(self) -> None:
        D.NDOE = int(input.readline())
        D.EDGE = int(input.readline())
        self._init_graph()
        tmp1, tmp2 = map(int, input.readline().split())
        D.START, D.END = tmp1 - 1, tmp2 - 1

    def _init_graph(self):
        """ 그래프 데이터 받기 """
        for i in range(D.NDOE):
            D.GRAPH.append({i:0})

        # 정답 데이터 저장
        D.PATH = [InF for _ in range(D.NDOE)]

        # 데이터 받기
        for _ in range(D.EDGE):
            go, end, weight = map(int, input.readline().split())
            if (key := end - 1) in D.GRAPH[go - 1].keys():
                if D.GRAPH[go - 1][key] <= weight: continue
            D.GRAPH[go - 1][key] = weight

    def _dijkstra(self):
        """ 다익스트라 알고리즘 """
        queue = []
        heapq.heappush(queue, (0, D.START))

        while queue:
            weight, cnode = heapq.heappop(queue)

            for nnode, nweight in D.GRAPH[cnode].items():
                if D.PATH[nnode] <= (tmp_weight := weight + nweight): continue # 0보다 크거나 같고
                D.PATH[nnode] = tmp_weight
                heapq.heappush(queue, (tmp_weight, nnode))

    def run(self) -> None:
        self._dijkstra()
        print(D.PATH[D.END])


if __name__ == '__main__':
    # input = open('./1916.txt')
    P = P()
    P.run()