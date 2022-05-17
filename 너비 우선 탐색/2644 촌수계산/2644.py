"""
    Solution code for "BaekJoon 촌수 계산".

    - Problem link: https://www.acmicpc.net/problem/
"""
from sys import stdin as input
from collections import deque


class N:
    COUNT: int
    START: int
    END: int
    EDGE_COUNT: int
    EDGE: list[list[int]]


class P:

    def __init__(self) -> None:
        N.COUNT = int(input.readline())
        N.START, N.END = map(int, input.readline().split())
        self._init_edge()

    def _init_edge(self):
        """ N.EDGE_COUNT """
        N.EDGE_COUNT = int(input.readline())
        N.EDGE = [[] for _ in range(N.COUNT + 1)]
        for _ in range(N.EDGE_COUNT):
            start, end = map(int, input.readline().split())
            N.EDGE[start].append(end)
            N.EDGE[end].append(start)

    def _bfs(self):
        """ 우선 넓이 탐색 """
        q = deque([N.START])
        check = [0 for _ in range(N.COUNT + 1)]
        check[N.START] = 1
        while q:
            cnode = q.popleft()
            for nnode in N.EDGE[cnode]:
                if check[nnode]: continue
                check[nnode] = check[cnode] + 1
                q.append(nnode)

        print(check[N.END] - 1)

    def run(self) -> None:
        self._bfs()


if __name__ == '__main__':
    # input = open('./2644.txt')
    P = P()
    P.run()