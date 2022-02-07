"""Solution code for "BaekJoon 모든 순열".

- Problem link: https://www.acmicpc.net/problem/10794
"""

from itertools import permutations
from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N = int(input.readline())

    def result(self) -> None:
        for anser in permutations([i for i in range(1, self.N + 1)]):
            print(*anser)

if __name__ == '__main__':
    # input = open('./10974.txt')
    P = P()
    P.result()