"""

    Solution code for "BaekJoon 어른 상어".

    - Problem link: https://www.acmicpc.net/problem/19237

    요구사항 주요 로직

    1. 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
    2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동 > 자신의 냄새를 그 칸에 뿌린다.
    3. 냄새는 상어가 k번 이동하고 나면 사라진다.

    이동 요구 사항
    1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. <우선순위 적용>
    2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. <우선순위 적용>
    3. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.

    4. 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

"""

from sys import stdin as input
from dataclasses import dataclass


@dataclass
class Go:
    """ 이동 방향 """
    direction = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]


@dataclass
class Shark:
    row: int # 상어 가로
    col: int # 상어 세로
    number: int # 상어 번호
    direction: int  # 현재 상어의 방향
    priority: list[list[int]] # 상어 우선순위

    def position(self):
        """ 상어 위치 출력 """
        return self.row, self.col, self.number


@dataclass
class Wather:
    shark_number: int # 상어 번호
    smell: int # 상어 냄새

    def __str__(self):
        return str(self.shark_number)


class P:

    def __init__(self) -> None:
        self.size, self.shark_count, self.smell = map(int, input.readline().split())
        self._init_sea()

    def _init_sea(self):
        """ 바다 생성자 """
        self.sea = []
        self.shark_position = {}
        shark_position = [0 for _ in range(self.shark_count)]  # 현재 상어 포지션

        # 바다 생성
        for row in range(self.size):
            tmp = list(map(int, input.readline().split()))
            row_tmp = []
            for col in range(self.size):
                row_tmp.append(Wather(shark_number=tmp[col], smell=0))
                if tmp[col] == 0: continue # 상어가 아니면 pass
                shark_position[tmp[col] - 1] = Shark(row=row, col=col, number=tmp[col], direction=0, priority=[])
            self.sea.append(row_tmp)

        # 현재 상어 보는 방향 받기

        for i, direction in enumerate(map(int, input.readline().split())):
            shark_position[i].direction = direction

        # 상어 우선순위 받기
        for i in range(self.shark_count):
            tmp_priority = []
            for _ in range(4):
                tmp_priority.append(list(map(int, input.readline().split())))
            shark_position[i].priority = tmp_priority

        # 상어 위치 기반으로 저장
        for shark in shark_position:
            row, col, _ = shark.position()
            self.shark_position[f"{row},{col}"] = shark

    def _push_smell(self):
        """ 상어 냄새 뿌리기 """
        for shark in self.shark_position.values():
            row, col, number = shark.position()
            self.sea[row][col].smell = self.smell
            self.sea[row][col].shark_number = number

    def _reduce_smell(self):
        """ 냄새 감소 """
        for row in range(self.size):
            for col in range(self.size):
                if self.sea[row][col].smell <= 0: continue

                self.sea[row][col].smell -= 1
                if self.sea[row][col].smell == 0:
                    self.sea[row][col].shark_number = 0

    def _go_no_smell(self, shark: Shark):
        """ 주변에 냄새가 없음 깨끗한 바다 찾기 """
        row, col, number = shark.position()
        direction = shark.direction - 1
        for priority in shark.priority[direction]:
            trow, tcol = Go.direction[priority - 1] # 이동 차이
            nrow, ncol = row + trow, col + tcol
            if not (0 <= nrow < self.size and 0 <= ncol < self.size): continue # 바다의 범위가 아니면 pass
            if self.sea[nrow][ncol].smell != 0: continue # 냄새가 0 이 아니면 pass

            # 기존에 존재할 경우
            if (nposition := f"{nrow},{ncol}") in self.shark_position_tmp.keys():
                if self.shark_position_tmp[nposition].number < number: # 기존에 상어에게 쫓겨남
                    return 0

            # 이동경로 변경
            shark.row, shark.col, shark.direction = nrow, ncol, priority
            self.shark_position_tmp[nposition] = shark
            return 0

        return -1

    def _go_smell(self, shark: Shark):
        """ 자신의 냄새 찾기 """
        row, col, number = shark.position()
        direction = shark.direction - 1
        for priority in shark.priority[direction]:
            trow, tcol = Go.direction[priority - 1] # 이동 차이
            nrow, ncol = row + trow, col + tcol
            if not (0 <= nrow < self.size and 0 <= ncol < self.size): continue # 바다의 범위가 아니면 pass
            if self.sea[nrow][ncol].shark_number != number: continue # 자신의 냄새와 다르면 pass

            # 기존에 존재할 경우
            if (nposition := f"{nrow},{ncol}") in self.shark_position_tmp.keys():
                if self.shark_position_tmp[nposition].number < number: # 기존에 상어에게 쫓겨남
                    return 0

            # 이동경로 변경
            shark.row, shark.col, shark.direction = nrow, ncol, priority
            self.shark_position_tmp[nposition] = shark
            return 0

        return -1

    def _move_shark(self):
        """ 상어 움직이기 """
        self.shark_position_tmp = {} # 상어 탬프
        for shark in self.shark_position.values():
            if self._go_no_smell(shark=shark) == 0: continue # 상어 냄새 없는 칸으로 움직임

            self._go_smell(shark=shark) # 자신이 왔던 곳으로 이동하기

        self.shark_position = self.shark_position_tmp # 상어 복사

    def _show_shark(self):
        """ 바다 확인하기 """
        for row in self.sea:
            print(" ".join(map(lambda x: str(x.shark_number), row)))
        print()

    def _show_smell(self):
        """ 바다 확인하기 """
        for row in self.sea:
            print(" ".join(map(lambda x: str(x.smell), row)))
        print()

    def _show_shark_position(self):
        """ 현재 상어 위치 """
        print(self.shark_position)

    def run(self) -> None:
        for i in range(1, 1_001):
            self._push_smell()
            self._move_shark()
            self._reduce_smell()

            if len(self.shark_position) == 1:
                print(i)
                return

        print(-1)
        return


if __name__ == '__main__':
    input = open('./19237.txt')
    P = P()
    P.run()