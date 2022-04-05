"""Solution code for "BaekJoon 어른 상어".

- Problem link: https://www.acmicpc.net/problem/19237
"""

from sys import stdin as input
from dataclasses import dataclass


class State:
    """ 물 상태 """
    water: int = 0

class Move:
    """ 이동 """

    DIRECTION_UP = 0
    DIRECTION_DOWN = 1
    DIRECTION_LEFT = 2
    DIRECTION_RIGHT = 3

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    GO = [UP, DOWN, LEFT, RIGHT]

class Shark:
    """ 상어 """
    smell: int = 0 # 냄새 수치
    all_count: int = 0 # 총 상어의 개수
    all_list: list[object] = [] # 모든 상어의 위치
    all_position: dict[str:int] = {}

    def __init__(self, row, col, number):
        # 위치
        self.row = row
        self.col = col

        self.life = True
        self.number = number  # 상어 번호
        self.direction = 0  # 상어 방향
        self.priority = []  # 우선순위


    def __repr__(self):
        return f"number={self.number}, row={self.row}, col={self.col}, direction={self.direction}"

    @property
    def position(self):
        """ 현재 상어 위치 """
        return self.row, self.col

    def next_move(self, next_direction: tuple[int, int]):
        """ 상어 다음 움직임 """
        row, col = next_direction
        return self.row + row, self.col + col

    def move(self, next_direction: tuple[int, int], type: int):
        """ 상어 움직임 """
        row, col = next_direction
        self.direction = type
        self.row += row
        self.col += col

    def back(self):
        """ 자신의 냄새 쪽으로 돌아가기 """

        # 방향 변경
        if self.direction == Move.DIRECTION_UP:
            self.direction = Move.DIRECTION_DOWN

        elif self.direction == Move.DIRECTION_DOWN:
            self.direction = Move.DIRECTION_UP

        elif self.direction == Move.DIRECTION_LEFT:
            self.direction = Move.DIRECTION_RIGHT

        elif self.direction == Move.DIRECTION_RIGHT:
            self.direction = Move.DIRECTION_LEFT

        row, col = Move.GO[self.direction]
        self.row, self.col = self.row + row, self.col + col

@dataclass
class Water:
    """ 냄새 """
    number: int  # 상어 번호
    concentration: int  # 냄새 농도

    def __str__(self):
        return str(self.concentration)

    def get_smell(self, number, concentration):
        """ 냄새 받기 """
        self.number = number
        self.concentration = concentration

    def smell_reduction(self):
        """ 냄새 감소 """
        if self.concentration <= 0:
            return
        self.concentration -= 1

        if self.concentration == 0:
            self.number = 0

class Aquarium:
    """ 아쿠아리움 데이터 클래스 """
    size: int = 0 # 아쿠아리움 싸이즈

    def __init__(self, state):
        self.state: list[list[int]] = state  # 아쿠아리움 상태


class P:

    def __init__(self):
        Aquarium.size, Shark.all_count, Shark.smell = map(int, input.readline().split())
        self._init_aquarium()
        self._init_direction()
        self._init_priority()

    def _init_aquarium(self):
        """ 아쿠아리움 데이터 생성 """

        Shark.all_list = [None for _ in range(Shark.all_count)] # 상어 개별 저장
        self.aquarium = [[Water(number=0, concentration=0) for _ in range(Aquarium.size)] # 아쿠아 리움 생성
                         for _ in range(Aquarium.size)]

        for row in range(Aquarium.size):
            tmp = map(int, input.readline().split())
            for col, state in enumerate(tmp):
                # 상어만 추출
                if state != State.water:
                    Shark.all_position[f"{row},{col}"] = state - 1
                    Shark.all_list[state - 1] = \
                        Shark(row=row, col=col, number=state)

    def _init_direction(self):
        """ 방향 받기 """
        for i, direction in enumerate(map(int, input.readline().split())):
            Shark.all_list[i].direction = direction - 1

    def _init_priority(self):
        """ 우선순위 받기 """
        for i in range(Shark.all_count): # 상어 선택
            tmp = []
            for _ in range(4): # 상하좌우 받기
                tmp.append(list(map(lambda x: int(x) - 1, input.readline().split())))
            Shark.all_list[i].priority = tmp

    def _show_smell(self):
        """ 아쿠아리움 확인 """
        for row in self.aquarium:
            print(" ".join(map(str, row)))
        print()

    def _show_shark_number(self):
        """ 아쿠아리움 확인 """
        for row in self.aquarium:
            print(" ".join(map(lambda x: str(x.number), row)))
        print()

    def _push_smell(self):
        """ 상어 냄새 풍기기 """
        for shark in Shark.all_list:
            row, col = shark.position
            self.aquarium[row][col]\
                .get_smell(number=shark.number, concentration=Shark.smell)

    def _smell_reduction(self):
        """ 냄새 감소 """
        for row in range(Aquarium.size):
            for col in range(Aquarium.size):
                self.aquarium[row][col].smell_reduction()

    def _move_shark(self):
        """ 상어 움직이기 """
        tmp_all_position = {}

        for i in range(Shark.all_count):
            if not Shark.all_list[i].life: continue # 상어 살아있는지 확인

            go_find = False
            # 냄새가 없는 곳 찾아서 이동
            for direction in Shark.all_list[i].priority[Shark.all_list[i].direction]:
                row_next, col_next = Shark.all_list[i].next_move(Move.GO[direction]) # 다음 움직이는 값 반환

                # 아쿠아 리움 범위인지 확인
                if not (0 <= row_next < Aquarium.size and 0 <= col_next < Aquarium.size): continue

                # 냄새가 0이 아니면 넘어감
                if self.aquarium[row_next][col_next].concentration != 0: continue
                
                # 상어 둘이 만나는지 확인
                key = f"{row_next},{col_next}"
                if key in tmp_all_position.keys(): # 상어가 겹치는 경우
                    if Shark.all_list[tmp_all_position[key]].number < Shark.all_list[i].number: # 기존의 상어 숫자가 작은 경우
                        Shark.all_list[i].life = False
                        go_find = True
                        break

                Shark.all_list[i].move(next_direction=Move.GO[direction], type=direction) # 진짜 움직임
                tmp_all_position[key] = Shark.all_list[i].number - 1
                go_find = True
                break

            # 냄새가 없는 곳 못찾은 경우
            if not go_find:
                Shark.all_list[i].back() # 뒤로 돌아가기
                row, col = Shark.all_list[i].position
                key = f"{row},{col}"
                tmp_all_position[key] = Shark.all_list[i].number - 1

        Shark.all_position = tmp_all_position

    def go(self):
        """ 1초 움직이기 """
        self._push_smell()
        self._move_shark()
        self._smell_reduction()

    def run(self):
        for i in range(1000):
            self.go()
            if len(Shark.all_position) == 1:
                print(1)
                break

            # if i == 4:
            #     self._show_smell()
            #     self._show_shark_number()
            #     break
        print(i)

if __name__ == '__main__':
    input = open('./19237.txt')
    P = P()
    P.run()