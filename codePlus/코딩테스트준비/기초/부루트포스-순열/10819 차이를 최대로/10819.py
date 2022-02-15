"""Solution code for "BaekJoon 차이를 최대로".

- Problem link: https://www.acmicpc.net/problem/10819
"""

from itertools import permutations
from sys import stdin as input

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.numbers = sorted(map(int, input.readline().split()))

    def _answer(self, num: list):
        tmp_sum = 0
        for i in range(0, self.N - 1):
            tmp_sum += abs(num[i] - num[i + 1])
        return tmp_sum

    def result(self) -> None:
        self.answer = 0
        for numbers in permutations(self.numbers):
            if self.answer < (tmp := self._answer(numbers)):
                self.answer = tmp

        print(self.answer)


if __name__ == '__main__':
    # input = open('./10819.txt')
    P = P()
    P.result()