"""
    Solution code for "BaekJoon 나이트의 이동".

    - Problem link: https://www.acmicpc.net/problem/7562
"""

from sys import stdin as input
from collections import deque


class N:
    """ 나이트 """

    row: int
    col: int
    arow: int
    acol: int

    MOVE = [
        (-2, 1),
        (-1, 2),

        (-2, -1),
        (-1, -2),

        (2, 1),
        (1, 2),

        (2, -1),
        (1, -2)
    ]


class B:
    """ 판 """
    N
    ANSWER: list[list[int]]


class D:
    """ 데이터 """
    TEST_CASE: int


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _input_data(self):
        """ 데이터 받기  """
        B.N = int(input.readline())
        N.row, N.col = map(int, input.readline().split())
        N.arow, N.acol = map(int, input.readline().split())
        D.ANSWER = [[0 for _ in range(B.N)] for _ in range(B.N)]

    def _bfs(self):
        """ 우선 너비 탐색 """
        q = deque([(N.row, N.col)])

        while q:
            crow, ccol = q.popleft()

            if crow == N.arow and ccol == N.acol:
                print(D.ANSWER[crow][ccol])
                break

            for go in N.MOVE:
                trow, tcol = go
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < B.N and 0 <= ncol < B.N): continue
                if D.ANSWER[nrow][ncol]: continue
                D.ANSWER[nrow][ncol] = D.ANSWER[crow][ccol] + 1
                q.append((nrow, ncol))


    def run(self) -> None:
        for _ in range(D.TEST_CASE):
            self._input_data()
            self._bfs()


if __name__ == '__main__':
    # input = open('./7562.txt')
    P = P()
    P.run()