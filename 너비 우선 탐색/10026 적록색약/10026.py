"""
    Solution code for "BaekJoon 적록색약".

    - Problem link: https://www.acmicpc.net/problem/10026
"""
from sys import stdin as input
from collections import deque


class S:
    NORMAL = 0
    RG = 1


class B:
    N: int
    borad = []
    chcek = []


class M:
    ALL = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]


class P:

    def __init__(self) -> None:
        self._init_board()

    def _init_board(self):
        """ 판 정보 받기 """
        B.N = int(input.readline())
        for _ in range(B.N):
            B.borad.append(list(input.readline().strip()))

    def _bfs(self, type, row, col):
        """ 우선 넓이 탐색 """
        q = deque([(row, col)])
        color = B.borad[row][col]

        while q:
            crow, ccol = q.popleft()
            if B.chcek[crow][ccol]: continue
            B.chcek[crow][ccol] = True

            for go in M.ALL:
                trow, tcol = go
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < B.N and 0 <= ncol < B.N): continue
                if B.chcek[nrow][ncol]: continue

                # 정상
                if type == S.NORMAL:
                    if B.borad[nrow][ncol] != color: continue

                # 적록 색약
                elif type == S.RG:
                    # 적록
                    if color != "B" and B.borad[nrow][ncol] == "B": continue
                    # 파란색
                    if color == "B" and B.borad[nrow][ncol] != "B": continue

                q.append((nrow, ncol))

        return 1

    def run(self) -> None:
        """ 실행 """
        answer = []
        for type in [S.NORMAL, S.RG]:
            B.chcek = [[False for _ in range(B.N)] for _ in range(B.N)]
            count = 0
            for row in range(B.N):
                for col in range(B.N):
                    if B.chcek[row][col]: continue
                    count += self._bfs(type, row, col)
            answer.append(count)
        print(*answer)


if __name__ == '__main__':
    # input = open('./10026.txt')
    P = P()
    P.run()