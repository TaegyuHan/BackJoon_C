"""
    Solution code for "BaekJoon 구슬 탈출".

    - Problem link: https://www.acmicpc.net/problem/13459
"""


from sys import stdin as input
from dataclasses import dataclass
from collections import deque


@dataclass
class B:
    WALL = "#"
    GROUND = "."
    RED = "R"
    BLUE = "B"
    HOLE = "O"
    P_HOLE = (-1, -1)
    P_RED = (-1, -1)
    P_BLUE = (-1, -1)


@dataclass
class G:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    ALL = [UP, DOWN, LEFT, RIGHT]


class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.board = [list(input.readline().strip()) for _ in range(self.N)]

    def _check_ball(self):
        """ 공위치 확인하기 """

        for row in range(self.N):
            for col in range(self.M):
                if self.board[row][col] == B.WALL: continue
                if self.board[row][col] == B.GROUND: continue

                if self.board[row][col] == B.RED:
                    rrow, rcol = row, col
                elif self.board[row][col] == B.BLUE:
                    brow, bcol = row, col
                elif self.board[row][col] == B.HOLE:
                    hrow, hcol = row, col

        return ((rrow, rcol, 1), (brow, bcol, 1), (hrow, hcol))

    def _move(self, row, col, go):
        """ 공 움직임 """
        trow, tcol = go
        while True:
            nrow, ncol = (row + trow, col + tcol)
            # 벽이랑 만난 경우
            if self.board[nrow][ncol] == B.WALL:
                return (False, row, col)
            # 홀이랑 만난 경우
            if self.board[nrow][ncol] == B.HOLE:
                return (True, row, col)
            row, col = nrow, ncol

    def _moves(self):
        """ 공 움직이기 """
        B.P_BLUE, B.P_RED, B.P_HOLE = self._check_ball()
        d = deque([(B.P_BLUE, B.P_RED)])

        while d:
            red, blue = d.popleft()
            rrow, rcol, rcount = red
            brow, bcol, bcount = blue

            for go in G.ALL:
                nrcheck, nrrow, nrcol = self._move(rrow, rcol, go)
                nbcheck, nbrow, nbcol = self._move(brow, bcol, go)

                if nbcheck: continue # 파란공이 나갈경우 제외

                if rcount == 11: return 0

                if nrcheck: # 빨간 공이 나간 경우
                    return 1

                # 공이 겹친경우
                if nrrow == nbrow and nrcol == nbcol:
                    back_row, back_col = go
                    if rrow == brow: # 가로가 같은 경우
                        if abs(nrcol - rcol) > abs(nbcol - bcol): # 빨간공이 더 많이 움직임
                            nrcol -= back_col
                        else: # 파란공이 더 많이 움직임
                            nbcol -= back_col

                    elif rcol == bcol: # 세로가 같은 경우
                        if abs(nrrow - rrow) > abs(nbrow - brow): # 빨간공이 더 많이 움직임
                            nrrow -= back_row
                        else: # 파란공이 더 많이 움직임
                            nbrow -= back_row

                d.append(((nrrow, nrcol, rcount + 1), (nbrow, nbcol, bcount + 1)))

    def run(self) -> None:
        print(self._moves())


if __name__ == '__main__':
    # input = open('./13460.txt')
    P = P()
    P.run()