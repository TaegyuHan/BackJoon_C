"""Solution code for "BaekJoon 어른 상어".

- Problem link: https://www.acmicpc.net/problem/19237
"""

from sys import stdin as input
from dataclasses import dataclass


@dataclass
class Direction:
    UP: int = 0
    DOWN: int = 1
    LEFT: int = 2
    RIGHT: int = 3

    GO_UP = (-1, 0)
    GO_DOWN = (1, 0)
    GO_LEFT = (0, -1)
    GO_RIGHT = (0, 1)
    GO = [GO_UP, GO_DOWN, GO_LEFT, GO_RIGHT]


@dataclass
class Shark:
    row: int
    col: int
    number: int
    current_direction: int
    direction: list[list[int]]


@dataclass
class Smell:
    smell: int
    number: int

    def __str__(self):
        return str(self.smell)

    def __repr__(self):
        return self.smell


class P:

    def __init__(self) -> None:
        self.N, self.M, self.K = map(int, input.readline().split())
        self.sharks = {}
        self.smell_board = [[Smell(smell=0, number=0) for _ in range(self.N)] for _ in range(self.N)]

        self._init_aquarium()
        self._init_shark_current_direction()
        self._init_shark_direction()

        self.answer = 0

    def _init_aquarium(self):
        """ 수족관 데이터 받기 """
        for row in range(self.N):
            tmp = list(map(int, input.readline().split()))
            for col, number in enumerate(tmp):
                if number != 0:
                    self.sharks[f"{row},{col}"] = Shark(row=row, col=col, number=number, current_direction=0, direction=0)

    def _init_shark_current_direction(self):
        """ 상어 방향 받기 """
        directions = list(map(int, input.readline().split()))
        for key in self.sharks.keys():
            self.sharks[key].current_direction = \
                directions[self.sharks[key].number - 1] - 1

    def _init_shark_direction(self):
        """ 상어 우선순위 받기 """
        directions = []
        for i in range(self.M):
            tmp = []
            for _ in range(4):
                tmp.append(list(map(int, input.readline().split())))
            directions.append(tmp)

        for key in self.sharks.keys():
            self.sharks[key].direction = directions[self.sharks[key].number - 1]

    def _show_aquarium(self):
        """ 수족관 확인 """
        for row in self.aquarium:
            print(" ".join(map(str, row)))
        print()

    def _show_smell_board(self):
        """ 수족관 냄새 확인 """
        for row in self.smell_board:
            print(" ".join(map(str, row)))
        print()

    def _show_smell_number_board(self):
        """ 수족관 냄새 확인 """
        for row in self.smell_board:
            for col in row:
                print(col.number, end=" ")
            print()
        print()

    def _smell_board_decrease(self):
        """ 상어 냄새 감소 """
        for row in range(self.N):
            for col in range(self.N):
                if self.smell_board[row][col].smell != 0:
                    self.smell_board[row][col].smell -= 1

                if self.smell_board[row][col].smell == 0:
                    self.smell_board[row][col].number = 0


    def _push_smell(self):
        """ 냄새 뿌리기 """
        for key in self.sharks.keys():
            row, col = map(int, key.split(","))
            self.smell_board[row][col] = \
                Smell(smell=self.K, number=self.sharks[key].number)

    def _move_shark(self):
        """ 상어 이동하기 """
        tmp_sharks = {}
        for key in self.sharks.keys():
            cur_row, cur_col, cur_direction = \
                self.sharks[key].row, self.sharks[key].col, self.sharks[key].current_direction

            # 냄새 찾았는지 확인
            go_find = False

            # 냄새 없는 곳 찾기
            for num in self.sharks[key].direction[cur_direction]:

                direction = num - 1
                row_tmp, col_tmp = Direction.GO[direction]
                row, col = cur_row + row_tmp, cur_col + col_tmp

                # 아쿠아리움 범위 확인
                if not (0 <= row < self.N and 0 <= col < self.N):
                    continue

                # 냄새 존재 확인
                if self.smell_board[row][col].number != 0:
                    continue

                # 이동한 상어가 이미 있는 경우
                if (tmp_key := f"{row},{col}") in tmp_sharks:
                    if tmp_sharks[tmp_key].number < self.sharks[key].number: # 누가더 빠른 번호인지 확인
                        go_find = True
                        break

                # 상어 이동
                self.sharks[key].current_direction = direction
                self.sharks[key].row = row
                self.sharks[key].col = col
                tmp_sharks[tmp_key] = self.sharks[key]
                go_find = True
                break

            # 다시 돌아가야 하는 경우
            if not go_find:
                for direction, direction_position in enumerate(Direction.GO):
                    row_tmp, col_tmp = direction_position
                    row, col = cur_row + row_tmp, cur_col + col_tmp

                    # 아쿠아리움 범위 확인
                    if not (0 <= row < self.N and 0 <= col < self.N):
                        continue

                    # 자신이 왔던곳이 아니면 pass
                    if self.smell_board[row][col].number != self.sharks[key].number:
                        continue

                    # 자신이 왔던곳
                    self.sharks[key].current_direction = direction
                    self.sharks[key].row = row
                    self.sharks[key].col = col
                    tmp_sharks[f"{row},{col}"] = self.sharks[key]
                    break

        self.sharks = tmp_sharks

    def run(self) -> None:

        for _ in range(1_000): # 1,000초
            self.answer += 1

            self._push_smell()
            self._show_smell_number_board()
            self._move_shark()
            self._smell_board_decrease()

            if len(self.sharks) == 1:
                print(self.answer)
                return

        print(-1)

if __name__ == '__main__':
    input = open('./19237.txt')
    P = P()
    P.run()