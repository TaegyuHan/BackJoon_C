"""
    Solution code for "BaekJoon 영역 구하기".

    - Problem link: https://www.acmicpc.net/problem/2583
"""
from sys import stdin as input
from collections import deque


class B:
    """ 보드 """
    ROW: int
    COL: int
    COUNT: int
    visited: list[list[bool]]
    answer = []

    @staticmethod
    def show_borad():
        for row in B.visited:
            print(*row)

class M:
    ALL = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

class P:

    def __init__(self) -> None:
        B.ROW, B.COL, B.COUNT = map(int, input.readline().split())
        B.visited = [[0 for _ in range(B.COL)] for _ in range(B.ROW)]

    def _bfs(self, row, col):
        """ 우선 넓이 탐색 """
        q = deque([(row, col)])
        tmp = 0
        while q:
            crow, ccol = q.popleft()
            B.visited[crow][ccol] = 1
            tmp += 1

            for go in M.ALL:
                trow, tcol = go
                nrow, ncol = crow + trow, ccol + tcol
                if not (0 <= nrow < B.ROW and 0 <= ncol < B.COL): continue
                if B.visited[nrow][ncol]: continue
                B.visited[nrow][ncol] = 1

                q.append((nrow, ncol))

        B.answer.append(tmp)

    def _cover_up(self, cover):
        """ 덮개 덮기 """
        left_y, left_x, right_y, right_x = cover
        for col in range(left_y, right_y):
            for row in range(left_x, right_x):
                B.visited[row][col] = 1

    def run(self) -> None:
        # 덮개 덮기
        for _ in range(B.COUNT):
            cover = tuple(map(int, input.readline().split()))
            self._cover_up(cover)

        for row in range(B.ROW):
            for col in range(B.COL):
                if B.visited[row][col]: continue
                self._bfs(row, col)

        print(len(B.answer))
        print(*sorted(B.answer))


if __name__ == '__main__':
    # input = open('./2583.txt')
    P = P()
    P.run()