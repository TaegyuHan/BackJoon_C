"""Solution code for "BaekJoon 링크와 스타트".

- Problem link: https://www.acmicpc.net/problem/15661
"""
import sys
from sys import stdin as input
from itertools import combinations

class P:

    def __init__(self) -> None:
        # input data
        self.N = int(input.readline())
        self.board = [list(map(int, input.readline().split()))
                      for _ in range(self.N)]

    def result(self) -> None:
        board_sum = [sum(i) + sum(j) for i, j in zip(self.board, zip(*self.board))]
        total_sum = sum(board_sum) // 2
        answer = sys.maxsize
        for i in range(1, self.N):
            for c in combinations(board_sum[1:], i):
                answer = min(answer, abs(total_sum - sum(c)))
                if answer == 0:
                    print(answer)
                    return
        print(answer)


if __name__ == '__main__':
    # input = open('./15661.txt')
    P = P()
    P.result()