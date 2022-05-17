from sys import stdin as input
from collections import deque

class Board:
    def __init__(self):
        self.board = []
        self.N = 0
        self.M = 0
        self.result = -1

    def input_data(self):
        self.N, self.M = map(int, input.readline().split())
        for _ in range(self.N):
            self.board.append(list(map(int, list(input.readline().rstrip()))))

    def show_board(self):
        for row in self.board:
            print(" ".join(map(str, row)))

    def BPS(self):
        # 이동 방향
        direction_x = [-1, 1, 0, 0]
        direction_y = [0, 0, -1, 1]
        x, y = 0, 0

        # deque 생성
        dq = deque()
        dq.append((x, y))

        while dq:
            x, y = dq.popleft()

            # 현 위치에서 4방향 확인
            for i in range(4):
                next_x = x + direction_x[i]
                next_y = y + direction_y[i]

                # 보드 위에 없으면 제거
                if (next_x < 0 or next_x >= self.N) and \
                   (next_y < 0 or next_y >= self.N):
                    continue
                
                # 다음이 벽이면 넘어감
                if self.board[next_x][next_y] == 0:
                    continue

                # 벽이 아니면 이동
                if self.board[next_x][next_y] == 1:
                    self.board[next_x][next_y] = self.board[x][y] + 1
                    dq.append((next_x, next_y))

        return self.board[self.N - 1][self.M - 1]

    def print_result(self):

        print(self.BPS())
        self.show_board()


if __name__ == '__main__':
    input = open("2178.txt")
    BD = Board()
    BD.input_data()
    BD.print_result()