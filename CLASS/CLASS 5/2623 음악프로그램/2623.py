"""
    Solution code for "BaekJoon 음악 프로그램"

    - Problem link: https://www.acmicpc.net/problem/2623
"""

from sys import stdin as input
from collections import deque

class D:
    NODE: int
    EDGE: int
    GRAPH = []
    TS_CHECK = []
    TS_COUNT = []
    ANSWER = []


class P:

    def __init__(self) -> None:
        D.NODE, D.EDGE = map(int, input.readline().split())
        self._init_graph()

    def _init_graph(self):
        """ 그래프 데이터 받기 """
        for _ in range(D.NODE):
            D.TS_CHECK.append(False)
            D.TS_COUNT.append(0)
            D.GRAPH.append([])

        for _ in range(D.EDGE):
            count, *mans = map(int, input.readline().split())
            for i in range(count - 1):
                start, end = mans[i: i + 2]
                D.TS_COUNT[end - 1] += 1
                D.GRAPH[start - 1].append(end - 1)

    def _ts_sort(self):
        """ 위상 정렬 """
        for node, in_count in enumerate(D.TS_COUNT):
            if in_count != 0: continue # 0 아니면 pass
            if D.TS_CHECK[node]: continue # 끝났는지 확인

            d = deque([node])
            while d:
                cnode = d.popleft()
                D.TS_CHECK[cnode] = True
                D.ANSWER.append(cnode + 1)

                for nnode in D.GRAPH[cnode]:
                    D.TS_COUNT[nnode] -= 1
                    if D.TS_COUNT[nnode] != 0: continue
                    d.append(nnode)

    def run(self) -> None:
        self._ts_sort()
        if len(D.ANSWER) != D.NODE:
            print(0)
        else:
            print(*D.ANSWER)


if __name__ == '__main__':
    # input = open('./2623.txt')
    P = P()
    P.run()