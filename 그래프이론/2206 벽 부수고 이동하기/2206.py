"""Solution code for "BaekJoon 벽 부수고 이동하기".

- Problem link: https://www.acmicpc.net/problem/2206
"""

from sys import stdin as input
from collections import deque


class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.board = [list(input.readline().strip()) for _ in range(self.N)]

    def BFS(self, row, col):
        nr, nc = [0, 0, 1, -1], [1, -1, 0, 0]
        queue = deque([[row, col, 1, True]])
        result = -1

        while queue:
            r, c, count, check = queue.popleft()

            for i in range(4):
                next_r, next_c = nr[i] + r, nc[i] + c

                if 0 <= next_r < self.N and 0 <= next_c < self.M:

                    # 목적지 도착했을 때
                    if next_r == self.N - 1 and next_c == self.M - 1:
                        result = count + 1
                        break

                    # 0을 만났을 때
                    if self.board[next_r][next_c] == "0":
                        queue.append([next_r, next_c, count + 1, True])
                        continue

                    # 1을 만났고 벽을 아직 안부쉈을 때
                    if check and self.board[next_r][next_c] == "1":
                        queue.append([next_r, next_c, count + 1, False])
                        continue

                    # 1을 만났고 벽을 아직 안부쉈을 때
                    if check and self.board[next_r][next_c] == "1":
                        queue.append([next_r, next_c, count + 1, False])
                        continue

        return result


    def result(self) -> None:
        print(self.BFS(row=0, col=0))


if __name__ == '__main__':
    input = open('./2206.txt')
    P = P()
    P.result()