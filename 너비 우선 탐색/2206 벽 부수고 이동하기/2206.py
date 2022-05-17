"""
    Solution code for "BaekJoon 벽 부수고 이동하기".

    - Problem link: https://www.acmicpc.net/problem/2206
"""

from sys import stdin as input
from collections import deque


class S:
    """ 상태 """
    NO_BROKEN = 0
    BROKEN = 1


class M:
    """ 이동하기 """
    ALL = [
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 0)
    ]


class B:
    """ 판 """
    ROW: int
    COL: int
    BOARD: list[list[int]]
    ANSWER: list[list[int]]
    WALL = 1
    EMPTY = 0

    @staticmethod
    def show_no_broken():
        """ 안부순 경로 확인하기 """
        for row in range(B.ROW):
            for col in range(B.COL):
                print(B.ANSWER[row][col][S.NO_BROKEN], end=" ")
            print()
        print()

    @staticmethod
    def show_broken():
        """ 부순 경로 확인하기 """
        for row in range(B.ROW):
            for col in range(B.COL):
                print(B.ANSWER[row][col][S.BROKEN], end=" ")
            print()
        print()


class P:

    def __init__(self) -> None:
        B.ROW, B.COL = map(int, input.readline().split())
        B.BOARD = [list(map(int, list(input.readline().strip()))) for _ in range(B.ROW)]
        B.ANSWER = [[[0] * 2 for _ in range(B.COL)] for _ in range(B.ROW)]

    def _bfs(self):
        """ 우선 너비 탐색 """
        q = deque([(0, 0, S.NO_BROKEN)])
        B.ANSWER[0][0][S.NO_BROKEN] = 1

        while q:
            crow, ccol, broken = q.popleft()
            if (crow == B.ROW - 1) and (ccol == B.COL - 1):
                print(B.ANSWER[crow][ccol][broken])
                exit()
                break

            for trow, tcol in M.ALL:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < B.ROW and 0 <= ncol < B.COL): continue

                # 벽이 뚤려있고 아직 방문 안한 상태
                if B.BOARD[nrow][ncol] == 0\
                        and B.ANSWER[nrow][ncol][broken] == 0:
                    B.ANSWER[nrow][ncol][broken] = B.ANSWER[nrow][ncol][broken] + 1
                    q.append((nrow, ncol, broken))

                # 벽이 막혀있는 상태
                elif B.BOARD[nrow][ncol] == 1 \
                        and broken == 0:
                    B.ANSWER[nrow][ncol][S.BROKEN] = B.ANSWER[nrow][ncol][broken] + 1
                    q.append((nrow, ncol, S.BROKEN))

    def run(self) -> None:
        """ 실행 """
        self._bfs()
        B.show_no_broken()
        B.show_broken()
        print(-1)

if __name__ == '__main__':
    input = open('./2206.txt')
    P = P()
    P.run()