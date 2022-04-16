"""
    Solution code for "BaekJoon 온풍기 안녕!".

    - Problem link: https://www.acmicpc.net/problem/23289

    풀이
    1. 집에 있는 모든 온풍기 에서 바람이 한번 나옴 <구현완료>
    2. 온도가 조절됨 <구현 완료>
    3. 온도가 1이상인 가장 바깥쪽 칸의 온도가 1씩 감소 <구현>
    4. 초콜릿 하나 먹는다.
    5. 조사하는 모든칸의 온도가 K이상이 되었는지 검사.
        > 모든 칸의 온도가 K이상이면 테스트를 중단
        > 아니면 1.부터 다시 시작한다.
"""

from collections import deque
from sys import stdin as input
from dataclasses import dataclass


class S:
    """ State """
    BLANK = 0
    HEATER_OUT = 5
    HEATER_RIGHT = 0
    HEATER_LEFT = 1
    HEATER_UP = 2
    HEATER_DOWN = 3
    TEMPERATURE_CHECK = 5
    WALL_VERTICAL = 1
    WALL_HORIZONTAL = 0
    WALL = 1


class C:
    """ Check go """
    FIRST_GO = [
        (0, 1), # 오른쪽
        (0, -1), # 왼쪽
        (-1, 0), # 위
        (1, 0) # 아래
    ]

    # 온도 체크 벽 확인
    AROUND_CHECK = [
        (0, 0, 1), # 오른쪽
        (0, -1, 1), # 왼쪽
        (0, 0, 0), # 위
        (1, 0, 0), # 아래
    ]
    
    # 방향
    DIRECTION = [
        # 오른쪽
        [
            (-1, 1), # 위
            (0, 1), # 오른쪽
            (1, 1) # 아래
        ],
        # 왼쪽
        [
            (-1, -1), # 위
            (0, -1), # 왼쪽
            (1, -1) # 아래
        ],
        # 위
        [
            (-1, -1), # 왼쪽
            (-1, 0), # 위
            (-1, 1) # 오른쪽
        ],
        # 아래
        [
            (1, -1),  # 왼쪽
            (1, 0),  # 아래
            (1, 1)  # 오른쪽
        ]
    ]

    # 벽 확인
    WALL_CHECK = [
        # 오른쪽
        [
            [(0, 0, 0), (-1, 0, 1)], # 위
            [(0, 0, 1)], # 오른쪽
            [(1, 0, 0), (1, 0, 1)] # 아래
        ],
        # 왼쪽
        [
            [(0, 0, 0), (-1, -1, 1)],  # 위
            [(0, -1, 1)],  # 왼쪽
            [(1, 0, 0), (1, -1, 1)]  # 아래
        ],
        # 위
        [
            [(0, -1, 1), (0, -1, 0)],  # 왼쪽
            [(0, 0, 0)],  # 위
            [(0, 0, 1), (0, 1, 0)]  # 오른쪽
        ],
        # 아래
        [
            [(0, -1, 1), (1, -1, 0)],  # 왼쪽
            [(1, 0, 0)],  # 아래
            [(0, 0, 1), (1, 1, 0)]  # 오른쪽
        ]
    ]


@dataclass
class Thermometer:
    """ 온도계 """
    row: int
    col: int

    @property
    def info(self):
        """ 온도계 위치  """
        return self.row, self.col


@dataclass
class Heater:
    """ 온풍기 """
    row: int
    col: int
    direction: int

    @property
    def info(self):
        """ 히터정보 """
        return self.row, self.col, self.direction


class R:
    """ Room 룸페이지 """
    ROW: int
    COL: int
    MAX_TEMPERATURE: int
    WALL_COUNT: int
    CHEK_POSITION = []
    HEATER_LIST = []
    room = {
        "temperature": [],
        "1": [], # vertical
        "0": [] # horizontal
    }


class P:

    def __init__(self) -> None:
        R.ROW, R.COL, R.MAX_TEMPERATURE = map(int, input.readline().strip().split())
        self._init_room_state()

    def _init_room_state(self):
        """ 방 데이터 받기 """
        for key in R.room.keys():
            R.room[key] = [[0 for _ in range(R.COL)] for _ in range(R.ROW)]

        for row in range(R.ROW):
            room = list(map(int, input.readline().strip().split()))
            for col in range(R.COL):
                if room[col] == S.BLANK: continue # 빈공간
                if room[col] == S.TEMPERATURE_CHECK:
                    R.CHEK_POSITION.append(Thermometer(row, col))
                    continue
                R.HEATER_LIST.append(Heater(row, col, room[col] - 1))

        R.WALL_COUNT = int(input.readline().strip())
        for _ in range(R.WALL_COUNT):
            row, col, wall_type = map(int, input.readline().strip().split())
            if wall_type == S.WALL_HORIZONTAL:
                R.room["0"][row - 1][col - 1] = S.WALL
            elif wall_type == S.WALL_VERTICAL:
                R.room["1"][row - 1][col - 1] = S.WALL

    def _show_temperature(self):
        """ 온도 확인 """
        for row in R.room["temperature"]:
            print("\t".join(map(str, row)))
        print()

    def _show_horizontal_wall(self):
        """ 가로 벽 확인 """
        for row in R.room["0"]:
            print("\t".join(map(str, row)))
        print()

    def _show_vertical_wall(self):
        """ 세로 벽 확인 """
        for row in R.room["1"]:
            print("\t".join(map(str, row)))
        print()

    def _show_tmp_temperature(self):
        """ 히터 1개 온도 확인 """
        for row in self.tmp_temperature:
            print("\t".join(map(str, row)))
        print()

    def _wall_check(self, row, col, check):
        """ 벽 확인 """
        for wall in check:
            trow, tcol, wall_type = wall
            nrow, ncol = row + trow, col + tcol

            if not (0 <= nrow < R.ROW and 0 <= ncol < R.COL):
                return False

            if R.room[str(wall_type)][nrow][ncol] == S.WALL:
                return False
        return True

    def _heater_temperature_sum(self):
        """ 히터에서 나온 바람 더하기 """
        for row in range(R.ROW):
            for col in range(R.COL):
                R.room["temperature"][row][col] \
                    += self.tmp_temperature[row][col]

    def _heater_run(self, heater: Heater):
        """ 히터 1개 동작 """
        self.tmp_temperature = [[0 for _ in range(R.COL)] for _ in range(R.ROW)]

        row, col, direction = heater.info
        trow, tcol = C.FIRST_GO[direction]
        d = deque([(row + trow, col + tcol, direction, S.HEATER_OUT)])
        while d:
            air = d.popleft()
            row, col, direction, temperature = air

            self.tmp_temperature[row][col] = temperature

            if temperature == 1: continue

            for go, check in enumerate(C.WALL_CHECK[direction]):
                if not self._wall_check(row, col, check): continue # 확산 가능한지 확인
                trow, tcol = C.DIRECTION[direction][go]
                nrow, ncol = row + trow, col + tcol
                if not (0 <= nrow < R.ROW and 0 <= ncol < R.COL): continue  # 범위 찾기

                d.append((nrow, ncol, direction, temperature - 1))

        # self._show_tmp_temperature()
        self._heater_temperature_sum() # 히터 방에 온도 더하기

    def _heaters_run(self):
        """ 모든 히터 동작하기 """
        for heater in R.HEATER_LIST:
            self._heater_run(heater)

    def _check_around_temperature(self, row, col):
        """ 주변 온도 비교후 저장 """
        temperature = R.room["temperature"][row][col]
        for go, tmp in enumerate(C.FIRST_GO):
            trow, tcol = tmp
            nrow, ncol = row + trow, col + tcol

            # 범위 확인
            if not (0 <= nrow < R.ROW and 0 <= ncol < R.COL): continue

            # 벽 확인
            wrow, wcol, wall_type = C.AROUND_CHECK[go]
            if R.room[str(wall_type)][row + wrow][col + wcol] == S.WALL: continue

            # 자신의 온도가 다른 곳 보다 낮은 경우
            if R.room["temperature"][row][col] <= R.room["temperature"][nrow][ncol]: continue

            move = (R.room["temperature"][row][col]
                    - R.room["temperature"][nrow][ncol]) // 4
            self.tmp_temperature[nrow][ncol] += move
            temperature -= move

        self.tmp_temperature[row][col] += temperature

    def _temperature_control(self):
        """ 온도 조절 """
        self.tmp_temperature = [[0 for _ in range(R.COL)] for _ in range(R.ROW)]

        for row in range(R.ROW):
            for col in range(R.COL):
                self._check_around_temperature(row, col)

        # 조절한 온도 복사하기
        R.room["temperature"] = self.tmp_temperature

    def _temperature_decrease(self):
        """ 온도 감소 """
        for row in range(1, R.ROW - 1):
            if R.room["temperature"][row][0] > 0: R.room["temperature"][row][0] -= 1
            if R.room["temperature"][row][R.COL - 1] > 0: R.room["temperature"][row][R.COL - 1] -= 1
        for col in range(R.COL):
            if R.room["temperature"][0][col] > 0: R.room["temperature"][0][col] -= 1
            if R.room["temperature"][R.ROW - 1][col] > 0: R.room["temperature"][R.ROW - 1][col] -= 1

    def _temperature_check(self):
        """ 온도 체크 """
        for thermometer in R.CHEK_POSITION:
            row, col = thermometer.info
            if R.room["temperature"][row][col] < R.MAX_TEMPERATURE:
                return False
        return True

    def run(self) -> None:

        chocolate = 0
        while True:
            self._heaters_run()
            self._temperature_control()
            self._temperature_decrease()
            chocolate += 1
            if self._temperature_check():
                print(chocolate)
                return
            if chocolate > 100:
                print(101)
                return


if __name__ == '__main__':
    # input = open("./23289.txt")
    P = P()
    P.run()