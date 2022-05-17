"""
    Solution code for "BaekJoon 서로 다른 부분 문자열의 개수".

    - Problem link: https://www.acmicpc.net/problem/11478
"""

from sys import stdin as input
from itertools import permutations

class P:

    def __init__(self) -> None:
        self._string = input.readline().strip()

    def run(self) -> None:
        key = set()
        for i in range(1, len(self._string) + 1):
            for j in range(len(self._string)):
                key.add(self._string[j:j + i])

        print(len(key))


if __name__ == '__main__':
    # input = open('./11478.txt')
    P = P()
    P.run()