"""
    Solution code for "BaekJoon 벽 부수고 이동하기 4".

    - Problem link: https://www.acmicpc.net/problem/16946
"""

from sys import stdin as input
from collections import deque


class S:
    WALL = 1
    EMPTY = 0


class M:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    ALL = [UP, DOWN, LEFT, RIGHT]


class R:
    """ 판 """
    ROW: int
    COL: int
    room = []
    visited = []
    answer = []
    walls = []
    empty_check = []
    empty_count = {}

class P:

    def __init__(self) -> None:
        R.ROW, R.COL = map(int, input.readline().split())
        self._init_room()

    def _init_room(self):
        """ 방 데이터 받기 """
        R.visited = [[False for _ in range(R.COL)] for _ in range(R.ROW)]
        R.answer = [[0 for _ in range(R.COL)] for _ in range(R.ROW)]
        R.empty_check = [[0 for _ in range(R.COL)] for _ in range(R.ROW)]
        for row in range(R.ROW):
            tmp_row = list(map(int, list(input.readline().strip())))
            R.room.append(tmp_row)
            for col in range(len(tmp_row)):
                if tmp_row[col] == S.EMPTY: continue
                R.walls.append((row,col))

    def _bfs(self, row, col, number):
        """ 빈공간 크기 정해서 수치 만들기 """
        q = deque([(row, col)])
        empty_count = 0
        while q:
            crow, ccol = q.popleft()
            empty_count += 1
            R.visited[crow][ccol] = True
            R.empty_check[crow][ccol] = number

            for go in M.ALL:
                trow, tcol = go
                nrow, ncol = crow + trow, ccol + tcol
                if not (0 <= nrow < R.ROW and 0 <= ncol < R.COL): continue
                if R.visited[nrow][ncol]: continue
                if R.room[nrow][ncol] == S.WALL: continue # 벽 PASS
                R.visited[nrow][ncol] = True

                q.append((nrow, ncol))

        R.empty_count[f"{number}"] = empty_count

    def _empty_find(self):
        """ 빈공간찾기 """
        empty_number = 1
        for row in range(R.ROW):
            for col in range(R.COL):
                if R.visited[row][col]: continue # 이미 방문한곳 PASS
                if R.room[row][col] == S.WALL: # 벽 PASS
                    R.visited[row][col] = True
                    continue
                self._bfs(row, col, empty_number)
                empty_number += 1

    def _show_empty(self):
        """ empty_number 보여주기 """
        for row in R.empty_check:
            print(*row)

    def _show_answer(self):
        """ 정답 확인하기 """
        for row in R.answer:
            print("".join(map(str, row)))

    def _wall_around_check(self):
        """ 벽 주변확인하기 """
        for wall in R.walls:
            crow, ccol = wall
            around_check = set()
            wall_sum = 0
            for go in M.ALL:
                trow, tcol = go
                nrow, ncol = crow + trow, ccol + tcol
                if not (0 <= nrow < R.ROW and 0 <= ncol < R.COL): continue
                if (check_number := R.empty_check[nrow][ncol]) == S.EMPTY: continue
                if check_number in around_check: continue
                around_check.add(check_number)
                wall_sum += R.empty_count[str(check_number)]

            R.answer[crow][ccol] = (wall_sum + S.WALL) % 10

    def run(self) -> None:
        """ 실행 """
        self._empty_find()
        self._wall_around_check()
        self._show_answer()

if __name__ == '__main__':
    # input = open('./16946.txt')
    P = P()
    P.run()