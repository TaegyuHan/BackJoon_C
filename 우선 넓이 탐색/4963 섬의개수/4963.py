from sys import stdin as input
from collections import deque

class P4963:
    def __init__(self):
        self.W = 1
        self.H = 1
        self.board = []
        self.count = 0

    def input_data(self):
            self.W, self.H = map(int, input.readline().split())
            self.board = []
            for _ in range(self.H):
                self.board.append(list(map(int, input.readline().rstrip().split())))

    def check_land(self, i, j):

        visited = []
        dq = deque([(i, j)])
        while dq:
            next = dq.popleft()
            if next in visited:
                continue
            visited.append(next)
            i, j = next
            around_x = [-1, 0, 1]
            around_y = [-1, 0, 1]
            for x in around_x:
                for y in around_y:
                    next_x = x + i
                    next_y = y + j
                    if next_x < 0 or next_y < 0:
                        continue
                    if next_x >= self.H or next_y >= self.W:
                        continue
                    if self.board[next_x][next_y] == 1:
                        self.board[next_x][next_y] = -1
                        dq.append((next_x, next_y))
        self.count += 1

    def result(self):
        self.count = 0
        for i in range(self.H):
            for j in range(self.W):
                if self.board[i][j] == 1:
                    self.check_land(i, j)
        print(self.count)

if __name__ == "__main__":
    # input = open("./4963.txt")
    P = P4963()
    while True:
        P.input_data()
        if P.W == 0 and P.H == 0:
            break
        P.result()
