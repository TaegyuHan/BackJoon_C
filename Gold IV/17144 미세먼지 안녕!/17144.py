"""Solution code for "BaekJoon 미세먼지 안녕!"

- Problem link: https://www.acmicpc.net/problem/17144

 공기 청정기 회전 실행해야 한다.
"""


from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.R, self.C, self.T = map(int, input.readline().split())
        self.board = [list(map(int, input.readline().split())) for _ in range(self.R)]
        self.cleaner_position = {
            'UP': [0, 0],
            'DOWN': [0, 0]
        }
        self.spread_dust_board = []
        self.direct = 4

    def _reset_spread_dust_board(self):
        """ 먼지 확산 배열 데이터 초기화 """
        self.spread_dust_board = [[0 for _ in range(self.C)]
                                  for _ in range(self.R)]

    def _dust_board_copy(self):
        """ 퍼진 먼지 복사  """
        self.board = self.spread_dust_board.copy()

    def _air_cleaner_position_copy(self):
        """ 공기청정기 복사  """
        self.board[self.cleaner_position["UP"][0]][self.cleaner_position["UP"][1]] = -1
        self.board[self.cleaner_position["DOWN"][0]][self.cleaner_position["DOWN"][1]] = -1

    def _show_board(self):
        """ 보드 확인하기  """
        for row in self.board:
            print(" ".join(map(str, row)))

    def _show_spread_dust_board(self):
        """ 보드 확인하기  """
        for row in self.spread_dust_board:
            print(" ".join(map(str, row)))

    def _dust_sum(self):
        """ 먼지의 총 양 """
        dusts = 0
        for row in self.spread_dust_board:
            dusts += sum(row)
        return dusts

    def _spread_dust(self, x: int, y: int, dust_value: int) -> int:
        """ 먼지 확산 하기 """

        # 보드안에 포함되어있는지 확인
        if not (0 <= x < self.R and 0 <= y < self.C):
            return -1 # 실패

        # 공기청정기 일때
        if self.board[x][y] == -1:
            return -1 # 실패

        # 먼지 확산
        self.spread_dust_board[x][y] += dust_value
        return 0 # 성공

    def _find_dust(self, x: int, y: int):
        """ 먼지 찾기 """
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        # 공기청정기 일때
        if self.board[x][y] == -1:
            return

        # 아무것도 없을 때
        if self.board[x][y] == 0:
            return

        # 먼지 확산 계산하기
        spread_value = self.board[x][y] // 5
        spread_count: int = 0
        for i in range(self.direct):
            nx = x + dx[i]
            ny = y + dy[i]
            if self._spread_dust(x=nx, y=ny, dust_value=spread_value) != -1:
                spread_count += 1

        # 확산하고 남은 먼지 추가
        self.spread_dust_board[x][y] += self.board[x][y] - (spread_value*spread_count)

    def _air_cleaner_find_position(self):
        """ 공기청정기 위치 찾기 """
        first = True
        for i in range(self.R):
            for j in range(self.C):
                if self.board[i][j] == -1:
                    if first == True:
                        self.cleaner_position["UP"] = [i, j]
                        first = False
                    else:
                        self.cleaner_position["DOWN"] = [i, j]

    def _air_cleaner_up(self, position: list):
        """ 공기청정기 위쪽 작동 """
        air_cleaner_x, air_cleaner_y = position[0], position[1]
        tmp_dust_value = 0

        # self._show_spread_dust_board(); print()

        # > 쪽으로 이동
        for col in range(air_cleaner_y + 1, self.C):
            # print(air_cleaner_x, col)
            tmp_dust_value, self.spread_dust_board[air_cleaner_x][col] = \
                self.spread_dust_board[air_cleaner_x][col], tmp_dust_value

        # self._show_spread_dust_board(); print()

        # ^ 쪽으로 이동
        for row in range(air_cleaner_x - 1, -1, -1):
            # print(row, self.C - 1)
            tmp_dust_value, self.spread_dust_board[row][self.C - 1] = \
                self.spread_dust_board[row][self.C - 1], tmp_dust_value

        # self._show_spread_dust_board(); print()

        # < 쪽으로 이동
        for col in range(self.C - 2, -1, -1):
            # print(0, col)
            tmp_dust_value, self.spread_dust_board[0][col] = \
                self.spread_dust_board[0][col], tmp_dust_value

        # self._show_spread_dust_board(); print()

        # v 쪽으로 이동
        for row in range(1, air_cleaner_x):
            # print(row, 0)
            tmp_dust_value, self.spread_dust_board[row][0] = \
                self.spread_dust_board[row][0], tmp_dust_value

        # self._show_spread_dust_board(); print()
        # print(tmp_dust_value)


    def _air_cleaner_down(self, position: list):
        """ 공기청정기 아래쪽 작동 """
        air_cleaner_x, air_cleaner_y = position[0], position[1]
        tmp_dust_value = 0

        # > 쪽으로 이동
        for col in range(air_cleaner_y + 1, self.C):
            # print(air_cleaner_x, col)
            tmp_dust_value, self.spread_dust_board[air_cleaner_x][col] = \
                self.spread_dust_board[air_cleaner_x][col], tmp_dust_value

        # self._show_spread_dust_board(); print()

        # v 쪽으로 이동
        for row in range(air_cleaner_x + 1, self.R):
            # print(row, self.C - 1)
            tmp_dust_value, self.spread_dust_board[row][self.C - 1] = \
                self.spread_dust_board[row][self.C - 1], tmp_dust_value

        # self._show_spread_dust_board(); print()

        # < 쪽으로 이동
        for col in range(self.C - 2, -1, -1):
            # print(self.R - 1, col)
            tmp_dust_value, self.spread_dust_board[self.R - 1][col] = \
                self.spread_dust_board[self.R - 1][col], tmp_dust_value

        # self._show_spread_dust_board(); print()

        # ^ 쪽으로 이동
        for row in range(self.R - 2, air_cleaner_x, -1):
            # print(row, 0)
            tmp_dust_value, self.spread_dust_board[row][0] = \
                self.spread_dust_board[row][0], tmp_dust_value

        # self._show_spread_dust_board(); print()
        # print(tmp_dust_value)

    def _run_air_cleaner(self):
        """ 공기청정기 돌리기 """

        self._air_cleaner_up(
            self.cleaner_position["UP"]
        )

        self._air_cleaner_down(
            self.cleaner_position["DOWN"]
        )

    def _run(self):
        self._reset_spread_dust_board()

        for i in range(self.R):
            for j in range(self.C):
                self._find_dust(x=i, y=j)

        # 공기 청정기 돌리기
        self._run_air_cleaner()
        # self._show_spread_dust_board()
        self._dust_board_copy() # 복사

    def result(self) -> None:
        # self._show_board()
        self._air_cleaner_find_position() # 공기 청정기 위치 찾기
        for i in range(self.T):
            self._run() # 먼지 퍼지게 하기
            if i != self.T - 1:
                self._air_cleaner_position_copy() # 마지막은 공기청정기 뺀다.

        answer = self._dust_sum()
        print(answer)


if __name__ == '__main__':
    # input = open('./17144.txt')
    P = P()
    P.result()