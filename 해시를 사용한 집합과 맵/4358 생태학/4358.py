"""
    Solution code for "BaekJoon 생태학".

    - Problem link: https://www.acmicpc.net/problem/4358
"""

from sys import stdin as input
from collections import defaultdict

class P:

    def __init__(self) -> None:
        self._table = defaultdict(int)
        self._count = 0
        while key := input.readline().strip():
            self._table[key] += 1
            self._count += 1

    def run(self) -> None:
        for key in sorted(self._table.keys()):
            print(f"{key} {self._table[key] / self._count * 100:.4f}")

if __name__ == '__main__':
    # input = open('./4358.txt')
    P = P()
    P.run()