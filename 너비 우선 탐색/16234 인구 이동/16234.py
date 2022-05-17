"""
    Solution code for "BaekJoon 인구 이동".

    - Problem link: https://www.acmicpc.net/problem/16234
"""

from sys import stdin as input
from collections import deque


class M:
    LEN = 4
    X = [-1, 1, 0, 0]
    Y = [0, 0, 1, -1]


class B:
    """ 판 """
    N: int
    MIN: int
    MAX: int
    BOARD: list[list[int]]
    VISITED: list[list[bool]]

    @staticmethod
    def show_board():
        for row in B.BOARD:
            print(*row)

class P:

    def __init__(self) -> None:
        B.N, B.MIN, B.MAX = map(int, input.readline().split())
        B.BOARD = [list(map(int, input.readline().split())) for _ in range(B.N)]

    def _bfs(self, row, col):
        """ 우선 넓이 탐색 """
        count = 0
        tmp_sum = 0
        change_position = set()
        q = deque([(row, col)])
        while q:
            crow, ccol = q.popleft()
            if B.VISITED[crow][ccol]: continue
            B.VISITED[crow][ccol] = True
            change_position.add((crow, ccol))
            tmp_sum += B.BOARD[crow][ccol]

            for i in range(M.LEN):
                nrow, ncol = M.X[i] + crow, M.Y[i] + ccol
                if not (0 <= nrow < B.N and 0 <= ncol < B.N): continue
                if B.VISITED[nrow][ncol]: continue
                if not (B.MIN <= abs(B.BOARD[crow][ccol] - B.BOARD[nrow][ncol]) <= B.MAX): continue
                count += 1
                q.append((nrow, ncol))

        # 값 변경하기
        tmp_sum = int(tmp_sum / len(change_position))
        for row, col in change_position:
            B.BOARD[row][col] = tmp_sum

        return count

    def _check(self):
        B.VISITED = [[False for _ in range(B.N)] for _ in range(B.N)]
        check = 0
        for row in range(B.N):
            for col in range(B.N):
                if B.VISITED[row][col]: continue
                check += self._bfs(row, col)
        return check

    def run(self) -> None:
        count = 0
        while self._check():
            count += 1
            pass
        print(count)
        # B.show_board()

if __name__ == '__main__':
    # input = open('./16234.txt')
    P = P()
    P.run()