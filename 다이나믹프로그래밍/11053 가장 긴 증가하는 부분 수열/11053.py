"""Solution code for "BaekJoon 가장 긴 증가하는 부분 수열".

- Problem link: https://www.acmicpc.net/problem/11053
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.nums = list(map(int,input.readline().split()))
        self.DP = [0 for _ in range(self.N)]

    def _run_dp(self):
        for i in range(self.N):
            for j in range(i):
                if self.nums[i] > self.nums[j] and self.DP[i] < self.DP[j]:
                    self.DP[i] = self.DP[j]
            self.DP[i] += 1

    def result(self) -> None:
        self._run_dp()
        print(self.DP)


if __name__ == '__main__':
    input = open('./11053.txt')
    P = P()
    P.result()