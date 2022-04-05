"""Solution code for "BaekJoon 낚시왕".

- Problem link: https://www.acmicpc.net/problem/17143
"""

from sys import stdin as input
from dataclasses import dataclass


@dataclass
class Shark:
    """ 상어 데이터 클래스 """
    row: int
    col: int
    speed: int
    direction: int
    size: int

    @property
    def position(self) -> (int, int):
        """ 상어의 위치 """
        return self.row, self.col

    def __str__(self) -> str:
        """ 문자열로 변경시 상어의 크기 반환 """
        return str(self.size)


class P:
    NOT_SHARK = '-'
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

    def __init__(self) -> None:
        self.R, self.C, self.M = map(int, input.readline().split())
        self._init_shark()
        self.fishing_man_position: int = -1
        self.fishing_size_total: int = 0

    def _init_shark(self) -> None:
        """ 상어 받기 """
        self.sharks = {}
        for _ in range(self.M):
            r, c, s, d, z = map(int, input.readline().split())
            row, col = r - 1, c - 1
            self.sharks[f"{row},{col}"] = Shark(row=row, col=col, speed=s, direction=d, size=z)

    def _show_aquarium(self) -> None:
        """ 아쿠아 리움 확인하기 """
        aquarium: list[list[str]] = [[P.NOT_SHARK for _ in range(self.C)] for _ in range(self.R)]
        tmp = ["X" for _ in range(self.C)]

        if self.fishing_man_position != -1 and self.fishing_man_position < self.C:
            tmp[self.fishing_man_position] = "O"
            print("\t".join(tmp))
        else:
            print("\t".join(tmp))

        for shark in self.sharks.values():
            aquarium[shark.row][shark.col] = shark

        for row in aquarium:
            print("\t".join(map(str, row)))
        print()

    def _move_fishing_man(self) -> None:
        """ 낙시꾼 이동 """
        self.fishing_man_position += 1

    def _move_all_shark(self) -> None:
        """ 상어 이동 """
        self.tmp_sharks = {}
        for shark in self.sharks.values(): # 모든 상어

            # 시간복잡도 해결 그대로 돌아오는 연산 제거
            # 한바퀴 돌아서 그대로인것 찾기
            if shark.direction in (P.UP, P.DOWN):
                shark.speed = shark.speed % ((self.R - 1) * 2)
            elif shark.direction in (P.RIGHT, P.LEFT):
                shark.speed = shark.speed % ((self.C - 1) * 2)

            # 상어 움직임
            for _ in range(shark.speed):
                if shark.direction == P.UP: # 위
                    # 맨 위일 경우
                    if shark.row == 0:
                        shark.row += 1
                        shark.direction = P.DOWN # 방향 전환
                    # 맨 위가 아닐 경우
                    else:
                        shark.row -= 1

                elif shark.direction == P.DOWN: # 아래
                    # 맨 아래일 경우
                    if shark.row == self.R - 1:
                        shark.row -= 1
                        shark.direction = P.UP # 방향 전환
                    # 맨 아래가 아닐 경우
                    else:
                        shark.row += 1

                elif shark.direction == P.RIGHT: # 오른쪽
                    # 맨 오른쪽일 경우
                    if shark.col == self.C - 1:
                        shark.col -= 1
                        shark.direction = P.LEFT # 방향 전환
                    # 맨 오른쪽이 아닐일 경우
                    else:
                        shark.col += 1

                elif shark.direction == P.LEFT: # 왼쪽
                    # 맨 왼쪽일 경우
                    if shark.col == 0:
                        shark.col += 1
                        shark.direction = P.RIGHT # 방향 전환
                    # 맨 왼쪽이 아닐경우
                    else:
                        shark.col -= 1

            # 움직인 상어
            key = f"{shark.row},{shark.col}"
            if key not in self.tmp_sharks: # 기존에 상어가 있는지 확인
                self.tmp_sharks[key] = shark
                continue

            # 크기 비교
            if self.tmp_sharks[key].size > shark.size: # 기존의 상어가 큰경우
                continue
             # 새로운 상어가 큰경우
            self.tmp_sharks[key] = shark

        # self.tmp_sharks 생성
        self.sharks = self.tmp_sharks

    def _fishing(self) -> None:
        """ 낚시 하기 """
        for i in range(self.R):
            # 낚은 상어 제거
            key = f"{i},{self.fishing_man_position}"
            if key in self.sharks:
                self.fishing_size_total += self.sharks[key].size
                del self.sharks[key]
                return

    def run(self) -> None:
        for _ in range(self.C):
            self._move_fishing_man()
            self._fishing()
            self._move_all_shark()
            # self._show_aquarium()

        print(self.fishing_size_total)


if __name__ == '__main__':
    # input = open('./17143.txt')
    P = P()
    P.run()