"""
    Solution code for "BaekJoon 카드 놓기".

    - Problem link: https://www.acmicpc.net/problem/5568
"""

from sys import stdin as input
from itertools import permutations

class P:

    def __init__(self) -> None:
        self._N = int(input.readline())
        self._K = int(input.readline())

    def run(self) -> None:
        nums = []
        count = set()
        for _ in range(self._N):
            nums.append(int(input.readline()))

        for data in permutations(nums, self._K):
            count.add("".join(map(str, data)))
        print(len(count))

if __name__ == '__main__':
    # input = open('./5568.txt')
    P = P()
    P.run()