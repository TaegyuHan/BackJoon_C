# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.BOARD_SIZE = int(input.readline())
        self.board = [list(input.readline().strip()) for _ in range(self.BOARD_SIZE)]
        self.row, self.col = 0, 0
        self.check_string = ["", "", ""]
        self.answer = 0

    def _show_board(self):
        """보드 보여주기"""
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    def _find_line(self):
        """색이 같은 연속적인 사탕 수 찾기"""
        for string in self.check_string:
            # print(string)
            tmp_max = 1
            for i in range(1, len(string)):
                if string[i - 1] == string[i]:
                    tmp_max += 1
                else:
                    # print(self.answer, tmp_max)
                    self.answer = max(self.answer, tmp_max)
                    tmp_max = 1
                # print(self.answer, tmp_max)
                self.answer = max(self.answer, tmp_max)

    def _find_biggest_candy(self, change: str) -> None:
        """변경된 라인 문자열로 만들기"""
        if change == "right":
            for i in range(self.BOARD_SIZE):
                self.check_string[0] += self.board[self.row][i]
                self.check_string[1] += self.board[i][self.col]
                self.check_string[2] += self.board[i][self.col + 1]
            self._find_line()

        elif change == "down":
            for i in range(self.BOARD_SIZE):
                self.check_string[0] += self.board[self.row][i]
                self.check_string[1] += self.board[self.row + 1][i]
                self.check_string[2] += self.board[i][self.col]
            self._find_line()

        self.check_string = ["", "", ""]

    def _change_cnady_right(self) -> bool:
        """현위치의 사탕 오른쪽과 위치 변경"""
        # 서로 다를 때만 변경
        if self.board[self.row][self.col] == \
                self.board[self.row][self.col + 1]:
            return False

        # 오른쪽 변경
        self.board[self.row][self.col], self.board[self.row][self.col + 1] = \
            self.board[self.row][self.col + 1], self.board[self.row][self.col]
        # print("change_cnady_right")
        # self._show_board()
        # print()
        return True

    def _change_cnady_down(self) -> None:
        """현위치의 사탕 아래와 위치 변경"""
        # 마지막 row는 오른쪽만 비교
        if self.row >= self.BOARD_SIZE - 1:
            return False

        # 서로 다를 때만 변경
        if self.board[self.row][self.col] == \
                self.board[self.row + 1][self.col]:
            return False

        # 오른쪽 변경
        self.board[self.row][self.col], self.board[self.row + 1][self.col] = \
            self.board[self.row + 1][self.col], self.board[self.row][self.col]
        # print("change_cnady_down")
        # self._show_board()
        # print()
        return True

    def result(self) -> None:
        """결과 출력"""
        # self._show_board()
        for self.row in range(self.BOARD_SIZE):
            for self.col in range(self.BOARD_SIZE - 1):
                # print(self.row, self.col)
                if self._change_cnady_right():# 오른쪽과 변경
                    self._find_biggest_candy("right")
                    self._change_cnady_right()  # 다시 원상태로
                    self._find_biggest_candy("right")

                if self._change_cnady_down(): # 아래와 변경
                    self._find_biggest_candy("down")
                    self._change_cnady_down() # 다시 원상태로
                    self._find_biggest_candy("down")
        print(self.answer)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./3085.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)