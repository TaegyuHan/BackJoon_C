"""Solution code for "BaekJoon 평범한 배낭".

- Problem link: https://www.acmicpc.net/problem/12865
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N, self.K = map(int, input.readline().split())
        self.items = [[0, 0]]

        for _ in range(self.N):
            self.items.append(list(map(int, input.readline().split())))

        self.dp = [[0 for _ in range(self.K + 1)]
                   for _ in range(self.N + 1)]

    def _run_dp(self) -> None:
        for i in range(1, self.N + 1):
            for j in range(1, self.K + 1):
                weight, value = self.items[i][0], self.items[i][1]

                if j < weight:
                    self.dp[i][j] = self.dp[i - 1][j]
                else:
                    self.dp[i][j] = max(
                        value + self.dp[i - 1][j - weight],
                        self.dp[i - 1][j]
                    )

    def result(self) -> None:
        self._run_dp()
        print(self.dp[self.N][self.K])


if __name__ == '__main__':
    # input = open('./12865.txt')
    P = P()
    P.result()