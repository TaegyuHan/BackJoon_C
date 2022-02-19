"""Solution code for "BaekJoon 1, 2, 3 더하기 5".

- Problem link: https://www.acmicpc.net/problem/15990
"""
import sys
from sys import stdin as input

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.MAX = 100_001
        self.MOD = 1_000_000_009
        self.dp = [[0 for _ in range(3)]
                   for _ in range(self.MAX)]

        self.dp[1] = [1, 0, 0]
        self.dp[2] = [0, 1, 0]
        self.dp[3] = [1, 1, 1]

    def run_dp(self) -> None:
        for i in range(4, self.MAX):
            self.dp[i][0] = (self.dp[i - 1][1] + self.dp[i - 1][2]) % self.MOD
            self.dp[i][1] = (self.dp[i - 2][0] + self.dp[i - 2][2]) % self.MOD
            self.dp[i][2] = (self.dp[i - 3][0] + self.dp[i - 3][1]) % self.MOD

    def result(self) -> None:
        self.run_dp()
        for _ in range(self.N):
            index = int(input.readline())
            print(sum(self.dp[index]) % self.MOD)


if __name__ == '__main__':
    # input = open('./15990.txt')
    P = P()
    P.result()