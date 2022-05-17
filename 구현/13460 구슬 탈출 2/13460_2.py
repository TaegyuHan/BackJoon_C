"""
    Solution code for "BaekJoon 구슬 탈출 2".

    - Problem link: https://www.acmicpc.net/problem/13460

문제 핵심 사항
1. 움직이는 쪽에 가까이 있는 구슬이 먼저 움직인다.
2. 벽에 붙으면 멈춘다, 공에 붙으면 멈춘다.
3. 구멍에 들어가면 구슬이 사라진다.
4. 파란색 구슬이 떨어지면 거기서 끝이다.

"""

from sys import stdin as input
from collections import deque
from dataclasses import dataclass


@dataclass
class B:
    WALL = "#"
    GROUND = "."
    RED = "R"
    BLUE = "B"
    HOLE = "O"


@dataclass
class Move:
    UP = 0
    DONW = 1
    LEFT = 2
    RIGHT = 3
    ALL = [UP, DONW, LEFT, RIGHT]


class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self._init_board()

    def _init_board(self):
        """ 보드 데이터 받기 """
        self.board = []
        self.ball = [0, 0]
        for row in range(self.M):
            tmp = list(input.readline().strip())
            self.board.append(tmp)
            for col in range(self.N):
                if tmp[col] == B.HOLE: # 홀 범위 생성
                    self.hole = (row, col)
                    continue
                if tmp[col] == B.RED:  # 빨간공
                    self.ball[0] = (row, col, 1)
                if tmp[col] == B.BLUE:  # 파란공
                    self.ball[1] = (row, col, 1)

    def _go(self, row, col, go):
        """ 기울인 쪽으로 움직이기 """

        while True:
            if go == Move.UP:
                if f"{row - 1}{col}" in self.ball_tmp.keys(): return (False, row, col)
                if self.board[row - 1][col] == B.WALL: return (False, row, col)
                if self.board[row - 1][col] == B.HOLE: return (True, row - 1, col)
                row -= 1
            elif go == Move.DONW:
                if f"{row + 1}{col}" in self.ball_tmp.keys(): return (False, row, col)
                if self.board[row + 1][col] == B.WALL: return (False, row, col)
                if self.board[row + 1][col] == B.HOLE: return (True, row + 1, col)
                row += 1
            elif go == Move.LEFT:
                if f"{row}{col - 1}" in self.ball_tmp.keys(): return (False, row, col)
                if self.board[row][col - 1] == B.WALL: return (False, row, col)
                if self.board[row][col - 1] == B.HOLE: return (True, row, col - 1)
                col -= 1
            elif go == Move.RIGHT:
                if f"{row}{col + 1}" in self.ball_tmp.keys(): return (False, row, col)
                if self.board[row][col + 1] == B.WALL: return (False, row, col)
                if self.board[row][col + 1] == B.HOLE: return (True, row, col + 1)
                col += 1

    def _move(self):
        """ 공 움직이기 """
        d = deque([tuple(self.ball)])

        while True:
            red, blue = d.popleft()
            rrow, rcol, rcount = red
            brow, bcol, bcount = blue
            for GO in Move.ALL:
                self.ball_tmp = {}
                first_red = False

                # 위로 올라가는 경우
                if GO == Move.UP:
                    if rrow <= brow: first_red = True
                elif GO == Move.DONW:
                    if rrow >= brow: first_red = True
                elif GO == Move.LEFT:
                    if rcol <= bcol: first_red = True
                elif GO == Move.RIGHT:
                    if rcol >= bcol: first_red = True

                # 빨간색이 먼저 움직이는 경우
                if first_red == True:
                    rstate, rgrow, rgcol = self._go(rrow, rcol, GO)
                    if not rstate: self.ball_tmp[f"{rgrow},{rgcol}"] = B.RED
                    bstate, bgrow, bgcol = self._go(brow, bcol, GO)
                    if not bstate: self.ball_tmp[f"{bgrow},{bgcol}"] = B.BLUE
                else:
                    bstate, bgrow, bgcol = self._go(brow, bcol, GO)
                    if not bstate: self.ball_tmp[f"{bgrow},{bgcol}"] = B.BLUE
                    rstate, rgrow, rgcol = self._go(rrow, rcol, GO)
                    if not rstate: self.ball_tmp[f"{rgrow},{rgcol}"] = B.RED

                if bstate == True: continue # 파란색 공이 빠진 경우

                if rstate == True: return rcount # 빨간색 공만 빠진경우 정답

                d.append(((rgrow, rgcol, rcount + 1), (bgrow, bgcol, bcount + 1)))

            if bcount == 5:
                break

    def run(self) -> None:
        print(self._move())
        pass


if __name__ == '__main__':
    input = open('./13460.txt')
    P = P()
    P.run()