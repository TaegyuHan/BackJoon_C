"""Solution code for "BaekJoon 전쟁 - 전투".

- Problem link: https://www.acmicpc.net/problem/1303
"""

from sys import stdin as input
from collections import deque


class P:
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)
    DIRECTION = [LEFT, RIGHT, UP, DOWN]
    MY_SOLDER = "W"
    ENEMY_SOLDER = "B"

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.field = [list(input.readline().strip()) for _ in range(self.M)]
        self.field_check = [[True for _ in range(self.N)] for _ in range(self.M)]
        self.W, self.B = 0, 0

    def _show_field(self) -> None:
        """ 전쟁터 확인 """
        for row in self.field:
            print(" ".join(row))

    def _show_field_check(self) -> None:
        """ 전쟁터 인원 확인판
            0 : 확인 안함
            1 : 확인 함
        """
        for row in self.field_check:
            print(" ".join(map(str, map(int, row))))

    def _check_surroundings(self, row: int, col: int) -> (int, str):
        """ 병사의 주변의 동일한 타입 확인

        :param row: 행
        :param col: 열

        :return: (int, str) : (병사의 수, 병사 타입)
        """

        soldier_count = 1
        soldier_type = self.field[row][col]
        d = deque([(row, col)]) # deque

        while d:
            current_row, current_col = d.popleft()
            # 확인 완료
            self.field_check[current_row][current_col] = False

            for sur_row, sur_col in P.DIRECTION:
                tmp_row, tmp_col = current_row + sur_row, current_col + sur_col

                # 필드에 포함하는지
                if not (0 <= tmp_row < self.M and 0 <= tmp_col < self.N):
                    continue # 포함 안함

                # 이미 확인한 필드인지
                if not self.field_check[tmp_row][tmp_col]:
                    continue # 포함 안함

                # 현재 같은 타입 아닌지
                if self.field[tmp_row][tmp_col] != soldier_type:
                    continue  # 포함 안함

                # 현재 같은 타입
                self.field_check[tmp_row][tmp_col] = False # 확인 완료
                soldier_count += 1
                d.append((tmp_row, tmp_col))

        return soldier_count, soldier_type

    def _soldier_power_save(self, soldier_count: int, soldier_type: str) -> None:
        """ 병사 위력 저장 """
        if soldier_type == P.MY_SOLDER:
            self.W += soldier_count**2
        elif soldier_type == P.ENEMY_SOLDER:
            self.B += soldier_count**2

    def _check_soldier(self) -> None:
        """ 병사 확인 """
        for row in range(self.M):
            for col in range(self.N):

                # 이미 확인한 병사인지 확인
                if not self.field_check[row][col]:
                    continue # 확인했던 병사는 pass

                # 병사의 주변 확인
                soldier_count, soldier_type = self._check_surroundings(row=row, col=col)
                self._soldier_power_save(soldier_count, soldier_type)

    def run(self) -> None:
        self._check_soldier()
        print(self.W, self.B)


if __name__ == '__main__':
    # input = open('./1303.txt')
    P = P()
    P.run()