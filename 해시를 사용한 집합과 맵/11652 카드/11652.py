"""
    Solution code for "BaekJoon 카드".

    - Problem link: https://www.acmicpc.net/problem/11652
"""

from sys import stdin as input
from collections import defaultdict


class P:

    def run(self) -> None:
        count = int(input.readline())
        dict_count = defaultdict(int)
        for _ in range(count):
            dict_count[int(input.readline())] += 1
        answer, _ = max(dict_count.items(), key=lambda x: (x[1], -x[0]))
        print(answer)


if __name__ == '__main__':
    # input = open('./11652.txt')
    P = P()
    P.run()