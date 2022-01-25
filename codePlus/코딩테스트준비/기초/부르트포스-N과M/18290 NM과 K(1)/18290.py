import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.row, self.col, self.find_count = map(int, input.readline().split())
        self.board = [list(map(int, input.readline().split()))
                      for _ in range(self.col)]

        self.pick_position = [(-1, -1) for _ in range(self.find_count)]
        self.pick_val = [0 for _ in range(self.find_count)]
        self.answer = None

    def _show_board(self) -> None:
        for row in self.board:
            print(" ".join(map(str, row)))

    def _check_pick(self, row: int, col: int) -> bool:
        check_list = [
            (row, col),
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

        for check_pick in check_list:
            if check_pick in self.pick_position:
                return False
        return True

    def _backtracking(self, count: int) -> None:
        if count == self.find_count:
            if self.answer == None:
                self.answer = sum(self.pick_val)
            else:
                self.answer = max(self.answer, sum(self.pick_val))
            return

        if count == 0:
            start_row, start_col = 0, 0
        else:
            start_row, start_col = self.pick_position[count]

        for row in range(start_row, self.row):
            for col in range(start_col, self.col):
                if self._check_pick(row, col) == True:
                    self.pick_position[count] = (row, col)
                    self.pick_val[count] = self.board[row][col]
                    self._backtracking(count + 1)
                    self.pick_position[count] = (-1, -1)

    def result(self) -> None:
        self._backtracking(count=0)
        print(self.answer)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./18290.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)
