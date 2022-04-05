"""
    Solution code for "BaekJoon 어른 상어".

    - Problem link: https://www.acmicpc.net/problem/19237
"""

from sys import stdin as input
# from copy import deepcopy

class P:

    # 상하 좌우 이동
    GO_ROW = [-1, 1, 0, 0]
    GO_COL = [0, 0, -1, 1]

    def __init__(self) -> None:
        self.size, self.shark_count, self.semll = map(int, input.readline().split())
        self._init_board()
        self.shark_direction = list(map(int, input.readline().split())) # 1차원 배열
        self.shark_priority = [[list(map(int, input.readline().split())) for _ in range(4)]
                               for _ in range(self.shark_count)] # 3차원 배열

    def _init_board(self):
        """ 아쿠아 리움 생성하기 """
        board = []
        self.shark_position = {}

        for row in range(self.size):
            tmp = list(map(int, input.readline().split()))
            board.append(tmp)
            for col in range(self.size):
                if tmp[col] != 0:
                    self.shark_position[f"{row},{col}"] = tmp[col] - 1

        self.board = {
            "number": board,
            "smell": [[0 for _ in range(self.size)] for _ in range(self.size)] # 2차원
        }

    def _push_semll(self):
        """ 상어가 냄새 출력 """
        for position in self.shark_position.keys():
            row, col = map(int, position.split(","))
            self.board["smell"][row][col] = self.semll # 냄새
            self.board["number"][row][col] = self.shark_position[position] + 1 # 상어 번호

    def _reduce_semll(self):
        """ 상어가 냄새 감소 """
        for row in range(self.size):
            for col in range(self.size):
                if self.board["smell"][row][col] > 0:
                    self.board["smell"][row][col] -= 1 # 냄새 감소
                    if self.board["smell"][row][col] == 0:
                        self.board["number"][row][col] = 0 # 상어 초기화

    def _move_shark(self):
        """ 상어 이동 """
        tmp_shark_position = {}
        for position in self.shark_position.keys():
            row, col = map(int, position.split(",")) # 상어 위치
            number = self.shark_position[position] # 상어 번호
            direction = self.shark_direction[number] - 1 # 방향
            not_move = True # 상어 이동 체크

            for go in self.shark_priority[number][direction]:

                nrow, ncol = row + P.GO_COL[go - 1], col + P.GO_ROW[go - 1]
                if not (0 <= nrow < self.size and 0 <= ncol < self.size): continue # 범위 체크

                if self.board["smell"][nrow][ncol] != 0: continue # 냄새가 존재 하는지 확인

                if (tmp_key := f"{nrow},{ncol}") in tmp_shark_position.keys(): # 상어가 만남 < 확인
                    if tmp_shark_position[tmp_key] < number: # 기존상어 번호가 더 작음
                        not_move = False
                        break # 다음 상어 움직임

                if number == 2:
                    print(number, go - 1, nrow, ncol)

                # 상어 이동
                tmp_shark_position[tmp_key] = number
                self.shark_direction[number] = go - 1
                not_move = False
                break  # 다음 상어 움직임

            # 이동 못한 상어 자신이 왔던 길로 다시 이동
            if not_move:
                print(direction)

        self.shark_position = tmp_shark_position

    def _show_board_number(self):
        """ 상어 숫자 판 보여주기 """
        for row in self.board["number"]:
            print(" ".join(map(str, row)))
        print()

    def _show_board_smell(self):
        """ 상어 냄새 판 보여주기 """
        for row in self.board["smell"]:
            print(" ".join(map(str, row)))
        print()

    def run(self) -> None:
        self._push_semll()
        self._show_board_smell()
        self._move_shark()

        # self._push_semll()
        # self._show_board_smell()
        #
        # self._show_board_number()

        # self._reduce_semll()
        # self._show_board_smell()
        # self._show_board_number()

if __name__ == '__main__':
    input = open('./19237.txt')
    P = P()
    P.run()