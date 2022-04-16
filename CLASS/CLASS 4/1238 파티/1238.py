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
    PATH = []


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

        D.PATH = [[InF for i in range(D.NODE)] for i in range(D.NODE)]

    def _show_path(self):
        """ 최단거리 정보 시각화 """
        for row in D.PATH:
            for col in row:
                if col == InF: print("InF", end="\t")
                else: print(col, end="\t")
            print()

    def _dijkstra(self, snode: int):
        """ 다익스트라 알고리즘 """
        queue = []
        heapq.heappush(queue, (0, snode))

        while queue:
            cweight, cnode = heapq.heappop(queue)
            for nweight, nnode in D.ROAD[cnode]:
                if D.PATH[snode][nnode] <= (tweight := cweight + nweight): continue
                D.PATH[snode][nnode] = tweight
                heapq.heappush(queue, (tweight, nnode))

    def _find_long_time_student(self):
        """ 가장 오래걸리는 학생 찾기 """
        answer = 0
        for i in range(D.NODE):
            if answer < (tmp_max := D.PATH[D.PARTY - 1][i] + D.PATH[i][D.PARTY - 1]):
                answer = tmp_max

        return answer

    def run(self) -> None:
        """ 실행 """
        for node_start in range(D.NODE):
            self._dijkstra(node_start)
        answer = self._find_long_time_student()
        print(answer)


if __name__ == '__main__':
    # input = open('./1238.txt')
    P = P()
    P.run()