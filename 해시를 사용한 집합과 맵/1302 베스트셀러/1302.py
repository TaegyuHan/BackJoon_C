"""
    Solution code for "BaekJoon 베스트 셀러".

    - Problem link: https://www.acmicpc.net/problem/1302
"""

from sys import stdin as input
from collections import defaultdict

class P:

    def __init__(self) -> None:
        self._count = int(input.readline())
        self._table = defaultdict(int)

    def run(self) -> None:
        max_tmp = 0
        for _ in range(self._count):
            key = input.readline().strip()
            self._table[key] += 1
            if max_tmp < self._table[key]:
                max_tmp = self._table[key]

        tmp = list(filter(lambda x: x[1] == max_tmp, self._table.items()))
        tmp.sort(key=lambda x: x[0])
        print(tmp[0][0])


if __name__ == '__main__':
    # input = open('./1302.txt')
    P = P()
    P.run()