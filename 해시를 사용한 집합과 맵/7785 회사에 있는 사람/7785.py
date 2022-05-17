"""
    Solution code for "BaekJoon 회사에 있는 사람".

    - Problem link: https://www.acmicpc.net/problem/7785
"""

from sys import stdin as input
from collections import defaultdict

class P:

    def __init__(self) -> None:
        self._count = int(input.readline())
        self._check_table = defaultdict(int)

    def run(self) -> None:
        for _ in range(self._count):
            name, in_or_out = input.readline().strip().split()
            if in_or_out == "enter":
                self._check_table[name] += 1
            elif in_or_out == "leave":
                del self._check_table[name]

        for name in sorted(self._check_table.keys(), reverse=True):
            print(name)


if __name__ == '__main__':
    # input = open('./7785.txt')
    P = P()
    P.run()