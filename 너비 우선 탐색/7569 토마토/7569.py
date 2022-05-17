"""
    Solution code for "BaekJoon 토마토".

    - Problem link: https://www.acmicpc.net/problem/7569
"""

from sys import stdin as input
from collections import deque

class M:
    ALL = [
        (0, 0, -1),
        (0, 0, 1),

        (1, 0, 0),
        (-1, 0, 0),

        (0, 1, 0),
        (0, -1, 0),
    ]

class S:
    """ 토마토 """
    TOMATO = 0
    RIPE_TOMATO = 1
    EMTPY = -1
    CHECK = 4

class B:
    """ 판 """
    X: int
    Y: int
    Z: int
    board = []
    tomato = 0
    pipe_tomatos = []

    @staticmethod
    def show_board():
        """ 판 확인하기 """
        for row in B.board:
            print(*row)


class P:

    def __init__(self) -> None:
        B.Y, B.X, B.Z = map(int, input.readline().split())
        self._init_board()

    def _init_board(self):
        """ 판 생성하기 """
        for z in range(B.Z):
            B.board.append([])
            for x in range(B.X):
                row = list(map(int, input.readline().strip().split()))
                B.board[z].append(row)
                for y in range(B.Y):
                    if row[y] == S.TOMATO: B.tomato += 1
                    if row[y] == S.RIPE_TOMATO:
                        B.pipe_tomatos.append((x, y, z))

    def _bfs(self):
        """ 우선 너비 탐색 """
        q = deque(B.pipe_tomatos)
        tmp_max = 0

        while q:
            cx, cy, cz = q.popleft()

            for go in M.ALL:
                tx, ty, tz = go
                nx, ny, nz = cx + tx, cy + ty, cz + tz
                if not (0 <= nx < B.X and 0 <= ny < B.Y and 0 <= nz < B.Z): continue
                if B.board[nz][nx][ny]: continue
                B.tomato -= 1
                B.board[nz][nx][ny] = B.board[cz][cx][cy] + 1
                if B.board[nz][nx][ny] > tmp_max: tmp_max = B.board[nz][nx][ny]
                q.append((nx, ny, nz))

        return tmp_max

    def run(self) -> None:
        """ 실행 """

        answer = self._bfs()
        if B.tomato: print(-1)
        else:
            if answer: print(answer - 1)
            else: print(answer)


if __name__ == '__main__':
    # input = open('./7569.txt')
    P = P()
    P.run()