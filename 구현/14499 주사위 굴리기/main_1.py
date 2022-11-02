"""
    Solution code for "BaekJoon 주사위 굴리기".

    - Problem link: https://www.acmicpc.net/problem/14499
"""
import heapq
from sys import stdin as input

DICE_SIZE = 6

MOVE = [
    0,  # TMP

    [0, 3, 4, 2, 5],  # 1

    [0, 3, 4, 6, 1],  # 2

    [0, 6, 1, 2, 5],  # 3

    [0, 1, 6, 2, 5],  # 4

    [0, 3, 4, 1, 6],  # 5

    [0, 3, 4, 5, 2],  # 6
]

UP_NUMBER = [
    0, # TMP
    6,
    5,
    4,
    3,
    2,
    1
]

MAP_MOVE = [
    0,  # TMP
    (0, 1),  # 오른쪽
    (0, -1),  # 왼쪽
    (-1, 0),  # 위
    (1, 0),  # 아래
]

EMPTY = 0
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


class Dice:

    def __init__(self, dice_position: tuple[int, int]):
        self.__point = [0 for _ in range(DICE_SIZE + 1)]
        self.__bottom = 1
        self.__row, self.__col = dice_position

    def move_position(self, direction: int):
        """ 이동 가능 확인 """
        trow, tcol = MAP_MOVE[direction]
        return self.__row + trow, self.__col + tcol

    def move(self, direction: int):
        """ 이동 """
        trow, tcol = MAP_MOVE[direction]
        self.__row = self.__row + trow
        self.__col = self.__col + tcol
        self.__bottom = MOVE[self.__bottom][direction]

    @property
    def up_value(self):
        """ 지도로 부터 위 """
        return self.__point[UP_NUMBER[self.__bottom]]

    @property
    def value(self):
        return self.__point[self.__bottom]

    @value.setter
    def value(self, value: int):
        self.__point[self.__bottom] = value


class Map:

    def __init__(self, board: list[list[int]], move_count: int, dice_position: tuple[int, int]):
        self.__map = board
        self.__row = len(board)
        self.__col = len(board[0])
        self.__move_count = move_count
        self.__dice = Dice(dice_position)

    def __in_check(self, position: tuple[int, int]):
        row, col = position
        if (0 <= row < self.__row and 0 <= col < self.__col):
            return True
        return False

    def __get_map_value(self, position: tuple[int, int]):
        row, col = position
        return self.__map[row][col]

    def __update_map_value(self, position: tuple[int, int], value: int):
        row, col = position
        self.__map[row][col] = value

    def __value_change(self, position: tuple[int, int]):
        """ 값 변경 """
        # map 이 0인 경우
        if (map_value := self.__get_map_value(position)) == EMPTY:
            self.__update_map_value(position, self.__dice.value)
            return
        # map이 0이 아닌경우
        self.__update_map_value(position, EMPTY)
        self.__dice.value = map_value

    def __move_or_hold(self, direction: int):
        """ 이동 혹은 멈춤 """
        position = self.__dice.move_position(direction)
        if not self.__in_check(position):
            return  # 멈춤
        # print(position)
        self.__dice.move(direction)
        self.__value_change(position)
        print(self.__dice.up_value)

    def dice_move(self):
        """ 주사위 움직이기 """
        for move in self.__move_count:
            # print(move)
            if move == RIGHT:
                self.__move_or_hold(RIGHT)
            elif move == LEFT:
                self.__move_or_hold(LEFT)
            elif move == UP:
                self.__move_or_hold(UP)
            elif move == DOWN:
                self.__move_or_hold(DOWN)


class P:
    __map: Map

    def __init__(self, file_name: str = "1.txt") -> None:
        """ 데이터 받기 """
        board = []
        with open(f"./data/input/{file_name}", encoding="utf-8") as input:
            row, col, srow, scol, move_count = map(int, input.readline().split())
            for _ in range(row):
                board.append(list(map(int, input.readline().split())))
            moves = list(map(int, input.readline().split()))
            self.__map = Map(board, moves, (srow, scol))

    def __logic(self):
        """ 풀이 """
        self.__map.dice_move()

    def answer(self) -> None:
        """ 정답 출력 """
        print(self.__logic())

    def answer_test(self) -> None:
        """ 테스트 정답 출력 """
        return self.__logic()


if __name__ == '__main__':
    p = P()
    p.answer()
