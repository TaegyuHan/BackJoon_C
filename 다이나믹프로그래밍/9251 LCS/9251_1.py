# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.INPUT_STIRNG_COUNT = 2
        self.string = {
            "one": f'0{input.readline().rstrip()}',
            "two": f'0{input.readline().rstrip()}'
        }
        self.board = [[0 for _ in range(len(self.string["one"]))] # + 1 빈 배열 추가
                         for _ in range(len(self.string["two"]))]

    def _show_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print()

    def _filling_board(self):
        for row in range(1, len(self.string["two"])):
            for col in range(1, len(self.string["one"])):

                # 문자가 같은경우
                if self.string["two"][row] == self.string["one"][col]:
                    self.board[row][col] = self.board[row - 1][col - 1] + 1
                else: # 문자가 다른경우
                    self.board[row][col] = max(
                        self.board[row - 1][col],
                        self.board[row][col - 1]
                    )

    def _find_LCS(self):
        col = len(self.board) - 1
        row = len(self.board) - 1
        answer = 0
        while (current := self.board[row][col]) != 0:
            # 둘이 같은 경우
            if self.string["two"][row] == self.string["one"][col]:
                # self.board[row][col] = "x"
                answer += 1
                row += -1
                col += -1
                continue # 대각선 위로 올라가기

            # 왼쪽의 수가 더 적은 경우
            elif current > self.board[row][col - 1]:
                row += -1
                continue # 위로 올라가기

            # 왼쪽의 수가 같은 경우
            else:
                col += -1
                continue  # 왼쪽으로 이동

        print(answer)

    def result(self) -> None:
        self._filling_board()
        self._find_LCS()
        self._show_board()



if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    input = open('./9251.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)