"""Solution code for "BaekJoon 가장 긴 증가하는 부분 수열 4".

- Problem link: https://www.acmicpc.net/problem/14002
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.nums = list(map(int, input.readline().split()))
        self.dp = [[0] for _ in range(self.N)]

    def result(self) -> None:
        for i in range(self.N):
            for j in range(i):
                if self.nums[i] > self.nums[j] and self.dp[i][-1] < self.dp[j][-1]:
                    self.dp[i] = self.dp[j]
            self.dp[i].append(self.nums[i])
            print(self.dp[i])

if __name__ == '__main__':
    input = open('./14002.txt')
    P = P()
    P.result()