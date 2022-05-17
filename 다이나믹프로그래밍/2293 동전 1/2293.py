"""Solution code for "BaekJoon 동전 1".

- Problem link: https://www.acmicpc.net/problem/2293
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N, self.K = map(int, input.readline().split())
        self.DP = [0 for _ in range(10_010)]
        self.coins = [0 for _ in range(10_010)]
        for i in range(1, self.N + 1):
            self.coins[i] = int(input.readline())

    def _run_dp(self):
        self.DP[0] = 1
        for i in range(1, self.N + 1):
            for j in range(self.coins[i], self.K + 1):
                self.DP[j] = self.DP[j] + self.DP[j - self.coins[i]]

    def result(self):
        self._run_dp()
        print(self.DP[self.K])


if __name__ == '__main__':
    # input = open('./2293.txt')
    P = P()
    P.result()