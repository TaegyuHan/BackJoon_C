"""
    Solution code for "BaekJoon 구슬 탈출 2".

- Problem link: https://www.acmicpc.net/problem/13460
"""

from sys import stdin as input
from dataclasses import dataclass
from collections import deque


@dataclass
class Move:
    """ 움직이기 """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 4
    ALL = [UP, DOWN, LEFT, RIGHT]


@dataclass
class State:
    """ 판 상태 """
    WALL: str = "#"
    GROUND: str = "."
    BLUE: str = "B"
    RED: str = "R"
    HOLE: str = "O"
    PASS = [WALL, GROUND]
    GOOL = (-1, -1)


class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self._init_board()

    def _init_board(self):
        """ 판 입력 받기 """
        self.board = []
        self.ball = {}
        for row in range(self.N):
            tmp = list(input.readline().strip())
            self.board.append(tmp) # 판 제작
            for col in range(self.M):
                if (state := tmp[col]) in State.PASS:
                    continue # 벽이거나 땅이면 PASS
                if state == State.HOLE:
                    State.GOOL = (row, col, state) # gool 지점
                    continue
                self.ball[state] = (row, col, 1)

    def _move(self, row: int, col: int, go: tuple[int, int]):
        """ 방향으로 직진하기 """
        if go == Move.UP: # 아래
            while True:
                if self.board[row][col] == State.HOLE:
                    return (True, row, col)
                if f"{row},{col}" in self.tmp_back: break
                if self.board[row - 1][col] == State.WALL: break
                row -= 1

        elif go == Move.DOWN: # 위쪽
            while True:
                if self.board[row][col] == State.HOLE:
                    return (True, row, col)
                if f"{row},{col}" in self.tmp_back: break
                if self.board[row + 1][col] == State.WALL: break
                row += 1

        elif go == Move.LEFT: # 왼쪽
            while True:
                if self.board[row][col] == State.HOLE:
                    return (True, row, col)
                if f"{row},{col}" in self.tmp_back: break
                if self.board[row][col - 1] == State.WALL: break
                col -= 1

        elif go == Move.RIGHT: # 오른쪽
            while True:
                if self.board[row][col] == State.HOLE:
                    return (True, row, col)
                if f"{row},{col}" in self.tmp_back: break
                if self.board[row][col + 1] == State.WALL: break
                col += 1

        return (False, row, col)

    def _find_directions(self):
        """ 판 움직이기
            BFS로 움직이기
        """
        d = deque([(self.ball[State.RED], self.ball[State.BLUE])])
        while d:

            red_ball, blue_ball = d.popleft()
            red_row, red_col, red_count = red_ball
            blue_row, blue_col, blue_count = blue_ball
            for go in Move.ALL:
                self.tmp_back = {}

                first_red = False
                # 빨간공 먼저 움직임
                # 위로 움직임
                if go == Move.UP and red_row < blue_row: first_red = True # 위로가는 경우 빨간공이 위에 있음
                elif go == Move.DOWN and red_row > blue_row: first_red = True # 아래로가는 경우 빨간공이 아래에 있음
                elif go == Move.LEFT and red_col < blue_col: first_red = True # 왼쪽으로가는 경우 빨간공이 왼쪽에 있음
                elif go == Move.RIGHT and red_col > blue_col: first_red = True # 오른쪽가는 경우 빨간공이 오른쪽에 있음

                # 파란공 먼저 움직임
                if first_red:
                    # 움직인 볼을 저장해야한다.
                    r_check, rrow, rcol = self._move(red_row, red_col, go)
                    if not r_check: self.tmp_back[f"{rrow},{rcol}"] = State.RED
                    b_check, brow, bcol = self._move(blue_row, blue_col, go)
                    if not b_check: self.tmp_back[f"{brow},{bcol}"] = State.BLUE

                else:
                    b_check, brow, bcol = self._move(blue_row, blue_col, go)
                    if not b_check: self.tmp_back[f"{brow},{bcol}"] = State.BLUE
                    r_check, rrow, rcol = self._move(red_row, red_col, go)
                    if not r_check: self.tmp_back[f"{rrow},{rcol}"] = State.RED

                if red_count == 10: return -1 # 정답을 못찾는 경우
                if b_check == True: continue
                if r_check == True and b_check == False: return red_count # 빨간색공 들어가고 파란색공 안들어감

                d.append([(rrow, rcol, red_count + 1), (brow, bcol, blue_count + 1)])

    def _show_board(self):
        """ 판 보여주기 """
        for row in self.board:
            print(" ".join(row))

    def run(self) -> None:
        print(self._find_directions())
        # self._show_board()
        pass

if __name__ == '__main__':
    input = open('./13460.txt')
    P = P()
    P.run()