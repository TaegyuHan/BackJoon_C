"""
    Solution code for "BaekJoon 배부른 마라토너".

    - Problem link: https://www.acmicpc.net/problem/10546
"""

from sys import stdin as input
from collections import defaultdict

class P:

    def __init__(self) -> None:
        self._count = int(input.readline())
        self._table = defaultdict(int)

        for _ in range(self._count):
            self._table[input.readline().strip()] += 1

        for _ in range(self._count - 1):
            name = input.readline().strip()
            self._table[name] -= 1
            if not self._table[name]: del self._table[name]

    def run(self) -> None:
        for answer in self._table.keys():
            print(answer)

if __name__ == '__main__':
    # input = open('./10546.txt')
    P = P()
    P.run()