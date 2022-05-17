"""
    Solution code for "BaekJoon 뱀".

    - Problem link: https://www.acmicpc.net/problem/3190
"""

from sys import stdin as input
from collections import deque


class D:
    """ 방향 변경 """
    RIGHT = "D"
    LEFT = "L"


class S:
    """ 상태 """
    EMPTY = "x"
    SNAKE = "-"
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class P:

    def __init__(self) -> None:
        self._N = int(input.readline())
        self._init_board() # 판 생성하기
        self._init_apple() # 사과 데이터 받기
        self._init_move() # 방향이동 데이터 받기

    def _init_board(self):
        """ 판 생성하기 """
        start = (0, 0)
        self._board = [[S.EMPTY for _ in range(self._N)] for _ in range(self._N)]
        self._snake = deque([start])
        self._board[0][0] = S.SNAKE
        self._snake_direction = S.RIGHT

    def _init_apple(self):
        """ 사과 받기 """
        self._apple_count = int(input.readline())
        self._apple_position = set(tuple(map(int, input.readline().split())) for _ in range(self._apple_count))

    def _init_move(self):
        """ 움직이는 데이터 받기 """
        self._move_count = int(input.readline())
        self._moves = deque([input.readline().strip().split() for _ in range(self._move_count)])

    def _show_board(self):
        """ 판 확인하기 """
        for row in range(self._N):
            for col in range(self._N):
                if (row + 1, col + 1) in self._apple_position:
                    print("O", end=" ")
                else:
                    print(self._board[row][col], end=" ")
            print()
        print()

    def _go_tmp(self):
        """ 앞으로 가는 이동 거리 """
        if self._snake_direction == S.UP: return (-1, 0)
        elif self._snake_direction == S.DOWN: return (1, 0)
        elif self._snake_direction == S.LEFT: return (0, -1)
        elif self._snake_direction == S.RIGHT: return (0, 1)

    def _change_check(self):
        """ 이동 확인하기  """
        # 이동이 남아있고 앞의 시간이 같으면
        if self._moves and self._time == int(self._moves[0][0]):
            self._change_direction(self._moves[0][1])
            self._moves.popleft()

    def _change_direction(self, direction):
        """ 방향 바꾸기 """
        if self._snake_direction == S.UP:
            if direction == D.RIGHT: self._snake_direction = S.RIGHT
            elif direction == D.LEFT: self._snake_direction = S.LEFT
        elif self._snake_direction == S.DOWN:
            if direction == D.RIGHT: self._snake_direction = S.LEFT
            elif direction == D.LEFT: self._snake_direction = S.RIGHT
        elif self._snake_direction == S.RIGHT:
            if direction == D.RIGHT: self._snake_direction = S.DOWN
            elif direction == D.LEFT: self._snake_direction = S.UP
        elif self._snake_direction == S.LEFT:
            if direction == D.RIGHT: self._snake_direction = S.UP
            elif direction == D.LEFT: self._snake_direction = S.DOWN

    def _snake_go(self):
        """ 뱀 이동하기 """
        hrow, hcol = self._snake[-1] # 뱀 머리
        trow, tcol = self._go_tmp() # 뱀 이동 방향및 거리
        nrow, ncol = hrow + trow, hcol + tcol

        # 벽을 만난 경우 멈춤
        # 꼬리를 만난 경우 멈춤
        if not (0 <= nrow < self._N and 0 <= ncol < self._N)\
                or self._board[nrow][ncol] == S.SNAKE:
            print(self._time)
            exit()
            return
        
        # 사과가 있으면
        if (apple := (nrow + 1, ncol + 1)) in self._apple_position:
            self._apple_position.remove(apple) # 사과 먹기
            self._snake.append((nrow, ncol)) # 뱀 크기 증가
            self._board[nrow][ncol] = S.SNAKE
            return

        # 사과가 없으면 > 뱀 이동
        drow, dcol = self._snake.popleft()
        self._board[drow][dcol] = S.EMPTY
        self._snake.append((nrow, ncol)) # 뱀 이동
        self._board[nrow][ncol] = S.SNAKE

    def run(self) -> None:
        self._time = 0 # 시간
        while True:
            self._time += 1
            self._snake_go()
            self._change_check()

        print(self._time)


if __name__ == '__main__':
    # input = open('./3190.txt')
    P = P()
    P.run()
