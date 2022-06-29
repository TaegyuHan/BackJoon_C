"""
    Solution code for "BaekJoon 벽 부수고 이동하기 2"

    - Problem link: https://www.acmicpc.net/problem/14442
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
# input = open('./14442.txt')


class M:
    """ 이동 """
    GO = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]


class D:
    """데이터 """
    ROW: int
    COL: int
    BREAK_COUNT: int
    board: list[list[int]]
    visited: list[list[int], list[int]]

    break_wall_count = 0

    WALL = "1"
    GROUND = "0"

    @classmethod
    def show_visited_board(cls):
        """ 방문판 보여주기 """
        for i, board in enumerate(cls.visited):
            print(i)
            for row in board:
                print(*row)
            print()

    @staticmethod
    def show_board():
        """ 판 보여주기 """


class P:

    def __init__(self) -> None:
        D.ROW, D.COL, D.BREAK_COUNT = map(int, input.readline().split())
        D.board = [list(input.readline().strip()) for _ in range(D.ROW)]
        D.END = (D.ROW - 1, D.COL - 1)
        D.visited = [[[0] * (D.BREAK_COUNT + 1) for _ in range(D.COL)]
                     for _ in range(D.ROW)]
        D.visited[0][0][D.BREAK_COUNT] = 1

    def _bfs(self):
        """ 너비 우선 탐색 """
        queue = deque([(0, 0, D.BREAK_COUNT)])

        while queue:
            crow, ccol, cvisited = queue.popleft()
            if crow == D.ROW - 1 and ccol == D.COL - 1:
                return D.visited[crow][ccol][cvisited]

            for trow, tcol in M.GO:
                nrow, ncol = trow + crow, tcol + ccol

                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                    continue

                # 벽이 있고, 부술수 있으며, 다음칸에 방문한 적이 없다.
                if D.board[nrow][ncol] == D.WALL \
                    and cvisited > 0 \
                    and D.visited[nrow][ncol][cvisited - 1] == 0:
                    D.visited[nrow][ncol][cvisited - 1] = D.visited[crow][ccol][cvisited] + 1
                    queue.append((nrow, ncol, cvisited - 1))

                # 벽이 없고, 다음칸이 방문한 적이 없다.
                if D.board[nrow][ncol] == D.GROUND and D.visited[nrow][ncol][cvisited] == 0:
                    D.visited[nrow][ncol][cvisited] = D.visited[crow][ccol][cvisited] + 1
                    queue.append((nrow, ncol, cvisited))
        return -1

    def run(self) -> None:
        """ 실행 """
        print(self._bfs())
        # D.show_visited_board()


if __name__ == '__main__':
    P = P()
    P.run()