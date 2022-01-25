# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N, self.M, self.K = map(int, input.readline().split())
        self.board = [list(map(int, input.readline().split()))
                           for _ in range(self.N)]

        self.visited = [[False for _ in range(self.M)]
                               for _ in range(self.N)]

        self.CHECK_LEN = 4
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

        self.answer = -10_000

    def _show_board(self) -> None:
        for row in self.board:
            print(" ".join(map(str, row)))

    def _check_visited(self, row: int, col: int) -> bool:
        for i in range(self.CHECK_LEN):
            check_row = row + self.dx[i]
            check_col = col + self.dy[i]

            # 범위 벗어나거나, 이미 존재하면
            if 0 <= check_row < self.N and 0 <= check_col < self.M:
                if self.visited[check_row][check_col] == True:
                    return False
        return True

    def _backtracking(self,
                      start_row: int, start_col: int,
                      index: int,  sum: int) -> None:

        if index == self.K:
            self.answer = max(self.answer, sum)
            return

        for row in range(start_row, self.N):
            for col in range(start_col if row == start_row else 0, self.M):
                # 방문했었는지 확인
                if self.visited[row][col]:
                    continue

                if self._check_visited(row, col) == True: # 이미 방문했는지 확인
                    self.visited[row][col] = True
                    self._backtracking(row, col, index + 1, sum + self.board[row][col])
                    self.visited[row][col] = False

    def result(self) -> None:
        # self._show_board()
        self._backtracking(start_row=0,
                           start_col=0,
                           index=0,
                           sum=0)
        print(self.answer)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./18290.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)