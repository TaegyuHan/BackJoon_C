"""
    Solution code for "BaekJoon 파티".

    - Problem link: https://www.acmicpc.net/problem/1238
"""

from sys import stdin as input
from sys import maxsize as InF
import heapq


class D:
    """ Data """
    NODE: int
    EDGE: int
    PARTY: int
    ROAD = [] # 길 저장


class P:

    def __init__(self) -> None:
        D.NODE, D.EDGE, D.PARTY = map(int, input.readline().split())
        self._init_road()

    def _init_road(self):
        """ 길 데이터 받기 """
        for i in range(D.NODE):
            D.ROAD.append([(0, i)])

        for _ in range(D.EDGE):
            start, end, weight = map(int, input.readline().split())
            D.ROAD[start - 1].append((weight, end - 1))

    def _dijkstra(self, snode: int):
        """ 다익스트라 알고리즘 """
        distance = [InF for _ in range(D.NODE)]
        queue = []
        heapq.heappush(queue, (0, snode))

        while queue:
            cweight, cnode = heapq.heappop(queue)
            for nweight, nnode in D.ROAD[cnode]:
                if distance[nnode] <= (tweight := cweight + nweight): continue
                distance[nnode] = tweight
                heapq.heappush(queue, (tweight, nnode))

        return distance

    def run(self) -> None:
        """ 실행 """
        answer = 0
        for node_start in range(D.NODE):
            go = self._dijkstra(node_start)
            back = self._dijkstra(D.PARTY - 1)
            answer = max(answer, go[D.PARTY - 1] + back[node_start])

        print(answer)


if __name__ == '__main__':
    # input = open('./1238.txt')
    P = P()
    P.run()