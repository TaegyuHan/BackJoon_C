"""
    Solution code for "BaekJoon 벽 부수고 이동하기".

    - Problem link: https://www.acmicpc.net/problem/2206
"""

from sys import stdin as input
from collections import deque


class S:
    """ 확인하기 """
    NO_BOKEN = 0
    BOKEN = 1


class G:
    LEN = 4
    X = [-1, 1, 0, 0]
    Y = [0, 0, -1, 1]


class B:
    """ 판 """
    ROW: int
    COL: int
    BOARD = []
    VISITED = []
    WALL = 1
    GROUND = 0

class P:

    def __init__(self) -> None:
        B.ROW, B.COL = map(int, input.readline().split())
        B.BOARD = [list(map(int, list(input.readline().strip()))) for _ in range(B.ROW)]
        B.VISITED = [[[0 for _ in range(B.COL)] for _ in range(B.ROW)] for _ in range(2)]

    def _bfs(self):
        """ 우선 넓이 탐색 """
        B.VISITED[S.NO_BOKEN][0][0] = 1
        q = deque([(S.NO_BOKEN, 0, 0)])

        while q:
            check, crow, ccol = q.popleft()

            if (crow == B.ROW - 1 and ccol == B.COL - 1):
                print(B.VISITED[check][crow][ccol])
                exit()

            for i in range(G.LEN):
                nrow, ncol = G.X[i] + crow, G.Y[i] + ccol
                if not (0 <= nrow < B.ROW and 0 <= ncol < B.COL): continue

                if B.BOARD[nrow][ncol] == B.WALL and check == S.NO_BOKEN:
                    B.VISITED[S.BOKEN][nrow][ncol] = B.VISITED[S.NO_BOKEN][crow][ccol] + 1
                    q.append((S.BOKEN, nrow, ncol))
                elif B.BOARD[nrow][ncol] == B.GROUND and B.VISITED[check][nrow][ncol] == 0:
                    B.VISITED[check][nrow][ncol] = B.VISITED[check][crow][ccol] + 1
                    q.append((check, nrow, ncol))


    def run(self) -> None:
        self._bfs()
        print(-1)


if __name__ == '__main__':
    # input = open('./2206.txt')
    P = P()
    P.run()