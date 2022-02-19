"""Solution code for "BaekJoon 카드 구매하기 2".

- Problem link: https://www.acmicpc.net/problem/16194
"""

from sys import stdin as input
from sys import maxsize

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.nums = [0] + list(map(int, input.readline().split()))

    def _show_data(self):
        print(self.nums)

    def result(self) -> None:
        for i in range(2, self.N + 1):
            for j in range(1, i):
                self.nums[i] = min(self.nums[i], self.nums[i - j] + self.nums[j])

        print(self.nums[-1])


if __name__ == '__main__':
    input = open('./16194.txt')
    P = P()
    P.result()