"""
    Solution code for "BaekJoon 온풍기 안녕!".

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

from sys import stdin as input
from collections import deque
from dataclasses import dataclass


@dataclass
class Room:
    """ 상태 """
    EMPTY: int = 0
    HEATER_RIGHT: int = 1
    HEATER_LEFT: int = 2
    HEATER_UP: int = 3
    HEATER_DONW: int = 4
    THERMOMETER: int = 5


@dataclass
class GO:
    """ 주변 확인 """
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

    P_RIGHT = (0, 1)
    P_LEFT = (0, -1)
    P_UP = (-1, 0)
    P_DOWN = (1, 0)
    ALL = [P_RIGHT, P_LEFT, P_UP, P_DOWN]


@dataclass
class HD:
    """ HeaterDirection 온풍기 방향 """

    FIRST_DIRECTION = [
        0, # 빈공간
        (0, 1), # 오른쪽
        (0, -1), # 왼쪽
        (-1, 0),  # 위
        (1, 0)  # 아래
    ]
    RIGHT = [
        (-1, 1),
        (0, 1),
        (1, 1)
    ]
    LEFT = [
        (-1, -1),
        (0, -1),
        (1, -1)
    ]
    UP = [
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ]
    DOWN = [
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    # 온도가 퍼지는 방향
    NEXT_DIRECTION = [
        0,
        RIGHT,
        LEFT,
        UP,
        DOWN
    ]

@dataclass
class Heater:
    """ 온풍기 """
    row: int # 가로 위치
    col: int # 세로 위치
    direction: int # 방향

    @property
    def info(self) -> tuple[int, int, int]:
        """ 히터 정보 """
        return self.row, self.col, self.direction


@dataclass
class Thermometer:
    """ 온도계 """
    row: int # 가로 위치
    col: int # 세로 위치

    @property
    def info(self) -> tuple[int, int, int]:
        """ 히터 정보 """
        return self.row, self.col

@dataclass
class Wall:
    """ 벽 """
    horizontal = 0
    vertical = 1

    row: int # 가로 위치
    col: int # 세로 위치
    direction: int  # 방향
        # 1 : 오른쪽
        # 0 : 위쪽


class P:

    def __init__(self) -> None:
        self.R, self.C, self.K = map(int, input.readline().split())
        self._init_room()
        self._init_wall()

    def _init_room(self) -> None:
        """ 방 데이터 받기 """
        self._room = []
        self._room_walls = []
        self._thermometers = []
        self._heaters = []
        for row in range(self.R):
            tmp_row = list(map(int, input.readline().split()))
            self._room.append([0 for row in range(self.C)])
            self._room_walls.append(["x" for row in range(self.C)])
            for col in range(self.C):
                if tmp_row[col] == Room.EMPTY: continue # 빈공간
                if tmp_row[col] == Room.THERMOMETER: # 온도계
                    self._thermometers.append(Thermometer(row=row, col=col))
                    continue
                # 히터
                self._heaters.append(Heater(row=row, col=col, direction=tmp_row[col]))

    def _init_wall(self) -> None:
        """ 벽 데이터 받기 """

        for _ in range(int(input.readline())):
            row, col, direction = map(int, input.readline().split())
            self._room_walls[row - 1][col - 1] = direction

    def _show_temperature_control_room(self):
        """ 기온 조절 확인하기 """
        for row in self._temperature_control_room:
            print("\t".join(map(str, row)))
        print()

    def _show_tmp_room(self):
        """ 히터 탬프 확인 """
        for row in self._tmp_room:
            print("\t".join(map(str, row)))
        print()

    def _show_walls(self):
        """ 방 벽 위치 보기 보기 """
        for row in self._room_walls:
            print("\t".join(map(str, row)))
        print()

    def _show(self):
        """ 방 온도 보기 """
        for row in self._room:
            print("\t".join(map(str, row)))
        print()

    def _tmp_room_push_room(self):
        """ 온도 더하기 """
        for row in range(self.R):
            for col in range(self.C):
                self._room[row][col] += \
                    self._tmp_room[row][col]

    def _down(self, row: int, col: int, direction: int):
        """ 히터 1개 아래 동작 """
        srow, scol = HD.FIRST_DIRECTION[direction]
        d = deque([(row + srow, col + scol, 5)])
        self._tmp_room = [[0 for _ in range(self.C)] for _ in range(self.R)]

        while d:
            row, col, temperature = d.popleft()
            if not (0 <= row < self.R and 0 <= col < self.C): continue

            self._tmp_room[row][col] = temperature
            if temperature == 1: continue

            # 왼쪽 아래 확인
            if (0 <= row + 1 < self.R and 0 <= col - 1 < self.C):
                if self._room_walls[row][col - 1] != Wall.vertical and \
                    self._room_walls[row + 1][col - 1] != Wall.horizontal:
                    d.append((row + 1, col - 1, temperature - 1))

            # 아래 확인
            if (0 <= row + 1 < self.R and 0 <= col < self.C):
                if self._room_walls[row + 1][col] != Wall.horizontal:
                    d.append((row + 1, col, temperature - 1))

            # 오른쪽 아래
            if (0 <= row + 1 < self.R and 0 <= col + 1 < self.C):
                if self._room_walls[row][col] != Wall.vertical and \
                    self._room_walls[row + 1][col + 1] != Wall.horizontal:
                    d.append((row + 1, col + 1, temperature - 1))

        self._tmp_room_push_room()

    def _up(self, row: int, col: int, direction: int):
        """ 히터 1개 위 동작 """
        srow, scol = HD.FIRST_DIRECTION[direction]
        d = deque([(row + srow, col + scol, 5)])
        self._tmp_room = [[0 for _ in range(self.C)] for _ in range(self.R)]

        while d:
            row, col, temperature = d.popleft()
            if not (0 <= row < self.R and 0 <= col < self.C): continue

            self._tmp_room[row][col] = temperature
            if temperature == 1: continue

            # 왼쪽 위 확인
            if (0 <= row < self.R and 0 <= col - 1 < self.C):
                if self._room_walls[row][col - 1] != Wall.vertical and \
                    self._room_walls[row][col - 1] != Wall.horizontal:
                    d.append((row - 1, col - 1, temperature - 1))

            # 위 확인
            if (0 <= row < self.R and 0 <= col < self.C):
                if self._room_walls[row][col] != Wall.horizontal:
                    d.append((row - 1, col, temperature - 1))

            # 오른쪽 위
            if (0 <= row < self.R and 0 <= col + 1 < self.C):
                if self._room_walls[row][col] != Wall.vertical and \
                    self._room_walls[row][col + 1] != Wall.horizontal:
                    d.append((row - 1, col + 1, temperature - 1))

        self._tmp_room_push_room()

    def _left(self, row: int, col: int, direction: int):
        """ 히터 1개 왼쪽 동작 """
        srow, scol = HD.FIRST_DIRECTION[direction]

        d = deque([(row + srow, col + scol, 5)])
        self._tmp_room = [[0 for _ in range(self.C)] for _ in range(self.R)]

        while d:
            row, col, temperature = d.popleft()
            if not (0 <= row < self.R and 0 <= col < self.C): continue

            self._tmp_room[row][col] = temperature
            if temperature == 1: continue

            # 왼쪽 위 확인
            if (0 <= row - 1 < self.R and 0 <= col - 1 < self.C):
                if self._room_walls[row - 1][col - 1] != Wall.vertical and \
                    self._room_walls[row][col] != Wall.horizontal:
                    d.append((row - 1, col - 1, temperature - 1))

            # 왼쪽 확인
            if (0 <= row < self.R and 0 <= col - 1 < self.C):
                if self._room_walls[row][col - 1] != Wall.vertical:
                    d.append((row, col - 1, temperature - 1))

            # 왼쪽 아래 확인
            if (0 <= row + 1 < self.R and 0 <= col - 1 < self.C):
                if self._room_walls[row + 1][col - 1] != Wall.vertical and \
                    self._room_walls[row + 1][col] != Wall.horizontal:
                    d.append((row + 1, col - 1, temperature - 1))

        self._tmp_room_push_room()

    def _right(self, row: int, col: int, direction: int):
        """ 히터 1개 오른쪽 동작 """
        srow, scol = HD.FIRST_DIRECTION[direction]

        d = deque([(row + srow, col + scol, 5)])
        self._tmp_room = [[0 for _ in range(self.C)] for _ in range(self.R)]

        while d:
            row, col, temperature = d.popleft()
            if not (0 <= row < self.R and 0 <= col < self.C): continue

            self._tmp_room[row][col] = temperature
            if temperature == 1: continue

            # 오른쪽 위 확인
            if (0 <= row - 1 < self.R and 0 <= col < self.C):
                if self._room_walls[row - 1][col] != Wall.vertical and \
                    self._room_walls[row][col] != Wall.horizontal:
                    d.append((row - 1, col + 1, temperature - 1))

            # 오른쪽 확인
            if (0 <= row < self.R and 0 <= col < self.C):
                if self._room_walls[row][col] != Wall.vertical:
                    d.append((row, col + 1, temperature - 1))

            # 오른쪽 아래 확인
            if (0 <= row + 1 < self.R and 0 <= col < self.C):
                if self._room_walls[row + 1][col] != Wall.vertical and \
                    self._room_walls[row + 1][col] != Wall.horizontal:
                    d.append((row + 1, col + 1, temperature - 1))

        self._tmp_room_push_room()

    def _heaters_run(self):
        """ 히터들 동작 """
        for heater in self._heaters:
            row, col, direction = heater.info
            if direction == Room.HEATER_RIGHT:
                self._right(row, col, direction)
            elif direction == Room.HEATER_LEFT:
                self._left(row, col, direction)
            elif direction == Room.HEATER_UP:
                self._up(row, col, direction)
            elif direction == Room.HEATER_DONW:
                self._down(row, col, direction)

    def _temperature_control(self, row: int, col: int) -> None:
        """ 현 위치의 온도 조절 """
        tmp_temperature = 0

        for i in range(4):
            trow, tcol = GO.ALL[i]
            nrow, ncol = trow + row, tcol + col
            if not (0 <= nrow < self.R and 0 <= ncol < self.C): continue

            # 오른쪽
            if i == GO.RIGHT:
                if self._room_walls[nrow][ncol] == Wall.vertical:
                    continue # 벽 확인
            # 왼쪽
            elif i == GO.LEFT:
                if self._room_walls[nrow][ncol] == Wall.vertical:
                    continue  # 벽 확인
            # 위
            elif i == GO.UP:
                if self._room_walls[nrow][ncol] == Wall.horizontal:
                    continue  # 벽 확인
            # 아래
            elif i == GO.DOWN:
                if self._room_walls[nrow][ncol] == Wall.horizontal:
                    continue  # 벽 확인

            # 차이 계산
            if self._room[row][col] < self._room[nrow][ncol]:
                tmp_cal = (self._room[nrow][ncol] - self._room[row][col]) // 4
                tmp_temperature += tmp_cal

        self._temperature_control_room[row][col] += \
            self._room[row][col] - tmp_temperature

    def _temperature_controls(self):
        """ 온도 조절 하기 """
        self._temperature_control_room = \
            [[0 for _ in range(self.C)] for _ in range(self.R)]

        for row in range(self.R):
            for col in range(self.C):
                self._temperature_control(row, col)

    def _decrease_temperature(self):
        """ 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소 """
        # 위
        for col in range(self.C):
            if self._temperature_control_room[0][col] > 0:
                self._temperature_control_room[0][col] -= 1
        # 아래
        for col in range(self.C):
            if self._temperature_control_room[self.R - 1][col] > 0:
                self._temperature_control_room[self.R - 1][col] -= 1
        # 왼쪽
        for row in range(1, self.R - 1):
            if self._temperature_control_room[row][0] > 0:
                self._temperature_control_room[row][0] -= 1
        # 오른쪽
        for row in range(1, self.R - 1):
            if self._temperature_control_room[row][self.C - 1] > 0:
                self._temperature_control_room[row][self.C - 1] -= 1

        self._room = self._temperature_control_room

    def _temperature_check(self):
        """  조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. """
        for thermometer in self._thermometers:
            row, col = thermometer.info
            if self._room[row][col] < self.K:
                return False
        return True

    def run(self) -> None:

        chocolate = 0
        while True:

            self._heaters_run()
            self._temperature_controls()
            self._decrease_temperature()

            chocolate += 1

            if chocolate == 1:
                self._show()
                break

            # if self._temperature_check():
            #     print(chocolate)
            #     self._show()
            #     break

            # if chocolate == 53:
            #     self._show()
            #     return

if __name__ == '__main__':
    input = open('./23289.txt')
    P = P()
    P.run()