from sys import stdin as input
from collections import deque

class P2667:
    def __init__(self):
        self.N = 0
        self.board = []

    def input_data(self):
        self.N = int(input.readline())
        self.board = [list(map(int, input.readline().rstrip())) for _ in range(self.N)]
        self.result_list = []

    def change_number_one(self, i, j):
        check_x = [1, 0, -1, 0]
        check_y = [0, 1, 0, -1]

        dq = deque([(i, j)])
        visited = set()

        while dq:
            ni, nj = dq.popleft()
            visited.add((ni, nj))
            for check_i in range(4):
                next_x = ni + check_x[check_i]
                next_y = nj + check_y[check_i]
                if next_x < 0 or next_y < 0:
                    continue
                if next_x >= self.N or next_y >= self.N:
                    continue
                if (next_x, next_y) in visited:
                    continue
                if self.board[next_x][next_y] == 1:
                    self.board[next_x][next_y] = -1
                    dq.append((next_x, next_y))

        self.result_list.append(len(visited))

    def check_group(self):
        for i in  range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 1:
                    self.change_number_one(i, j)

    def result(self):
        self.check_group()
        print(len(self.result_list))
        self.result_list.sort()
        for num in self.result_list:
            print(num)


if __name__ == '__main__':
    # input = open("./2667.txt")
    P = P2667()
    P.input_data()
    P.result()
