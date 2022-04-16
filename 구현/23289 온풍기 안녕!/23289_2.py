"""
    Solution code for "BaekJoon 온풍기 안녕".

    - Problem link: https://www.acmicpc.net/problem/23289

    풀이
    1. 집에 있는 모든 온풍기 에서 바람이 한번 나옴 <구현 완료>
    2. 온도가 조절됨 < >
    3. 온도가 1이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    4. 초콜릿 하나 먹는다.
    5. 조사하는 모든칸의 온도가 K이상이 되었는지 검사.
        > 모든 칸의 온도가 K이상이면 테스트를 중단
        > 아니면 1.부터 다시 시작한다.

"""
from sys import stdin as input; input = open('./23289.txt')
from collections import deque
from dataclasses import dataclass


@dataclass
class Heater:
    """ 히터 """
    row: int
    col: int
    direction: int

    @property
    def info(self):
        """ 히터 정보 """
        return self.row, self.col, self.direction

    def start(self):
        """ 히터 바람 시작하는곳 """
        nrow, ncol = Start.LIST[self.direction]
        start_temperature = 5
        return self.row + nrow, self.col + ncol, self.direction, start_temperature


@dataclass
class Thermometer:
    """ 온도계 """
    row: int
    col: int


class Start:
    """ 시작 방향 """
    RIGHT = (0, 1)
    LEFT = (0, -1)
    UP = (-1, 0)
    DOWN = (1, 0)
    LIST = [0, RIGHT, LEFT, UP, DOWN]

class State:
    """ 방 상태 """
    EMPTY = 0
    H_RIGHT = 1
    H_LEFT = 2
    H_UP = 3
    H_DOWN = 4
    THERMOMETER = 5


class WallCheck:
    """ 벽 존재 확인 """
    LIST = [0,# 첫번째 빈공간

        # 오른쪽
        [[(0, 0, 0), (-1, 0, 1)], # 위
         [(0, 0, 1)], # 중간
         [(1, 0, 0), (1, 0, 1)]], # 아래

        # 왼쪽
        [[(0, 0, 0), (-1, -1, 1)],  # 위
         [(0, -1, 1)],  # 중간
         [(-1, 0, 0), (-1, -1, 1)]],  # 아래
            
        # 위
        [[(0, -1, 1), (0, -1, 0)],  # 왼쪽
         [(0, 0, 0)],  # 위
         [(0, 0, 1), (0, 1, 0)]],  # 오른쪽
            
        # 아래
        [[(0, -1, 1), (-1, -1, 0)],  # 왼쪽
         [(-1, 0, 0)],  # 아래
         [(0, 0, 1), (-1, 1, 0)]]  # 오른쪽
    ]

    SUCCESS = [0, # 빈공간

       # 오른쪽
       [(-1, 1),  # 위
        (0, 1),  # 중간
        (1, 1)],  # 아래

       # 왼쪽
       [(-1, -1),  # 위
        (0, -1),  # 중간
        (1, -1)],  # 아래

       # 위
       [(-1, -1),  # 왼쪽
        (-1, 0),  # 위
        (-1, 1)],  # 오른쪽

       # 아래
       [(1, -1),  # 왼쪽
        (1, 0),  # 아래
        (1, 1)]  # 오른쪽
    ]

class Room:
    """ 방 """
    row: int
    col: int
    check_temperature: int
    state: list[list[int]] = []
    thermometers: list[Thermometer]= []
    heaters: list[Heater] = []
    walls = [[], []]


class P:

    def __init__(self):
        Room.row, Room.col, Room.check_temperature = \
            map(int, input.readline().split())
        self._init_room_state()
        self._init_walls()

    def _init_room_state(self):
        """ 방 상태 데이터 받기 """
        for row in range(Room.row):
            tmp = list(map(int, input.readline().split()))
            Room.state.append(tmp)
            for col in range(Room.col):
                if tmp[col] == State.EMPTY: continue
                if tmp[col] == State.THERMOMETER: # 온도계
                    Room.thermometers.append(Thermometer(row, col))
                    continue
                Room.heaters.append(Heater(row, col, tmp[col])) # 히터

    def _init_walls(self):
        """ 벽 생성 데이터 받기 """
        for i in range(2):
            Room.walls[i] = [[False for _ in range(Room.col)] for _ in range(Room.row)]

        for _ in range(int(input.readline())):
            row, col, state = map(int, input.readline().split())
            Room.walls[state][row - 1][col - 1] = True

    def _show_walls(self):
        """ 벽 보기 """
        for walls in Room.walls:
            for row in walls:
                print("\t".join(map(str, row)))
            print()

    def _show_tmp_temperaturer(self, room):
        """ 벽 보기 """
        for row in room:
            print("\t".join(map(str, row)))
        print()

    def _wall_check(self, row: int, col: int, check_list: int):
        """ 벽 확인 """
        for check in check_list:
            trow, tcol, wall_type = check
            nrow, ncol = row + trow, col + tcol
            if not (0 <= nrow < Room.row and 0 <= ncol < Room.col): continue
            if Room.walls[wall_type][nrow][ncol]:
                print(row, col)
                return False

        return True

    def _heater_run(self, heater: Heater):
        """ 1개 히터 실행 """
        tmp_temperaturer = [[0 for _ in range(Room.col)] for _ in range(Room.row)]
        d = deque([heater.start()])
        while d:
            row, col, direction, temperature = \
                d.popleft()

            tmp_temperaturer[row][col] = temperature
            if temperature == 1: continue

            for i, check_list in enumerate(WallCheck.LIST[direction]):
                if not self._wall_check(row, col, check_list): continue
                trow, tcol = WallCheck.SUCCESS[direction][i]
                nrow, ncol = row + trow, col + tcol
                if not (0 <= nrow < Room.row and 0 <= ncol < Room.col): continue
                d.append((nrow, ncol, direction, temperature - 1))

        self._show_tmp_temperaturer(tmp_temperaturer)

    def _heaters_run(self):
        """ 모든 히터 실행 """
        for heater in Room.heaters:
            self._heater_run(heater)
            break

    def run(self):
        """ 실행 """
        self._show_walls()
        self._heaters_run()

if __name__ == '__main__':
    P = P()
    P.run()