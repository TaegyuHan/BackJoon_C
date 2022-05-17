"""
    Solution code for "BaekJoon 카드 문자열".

    - Problem link: https://www.acmicpc.net/problem/13417
"""

from sys import stdin as input
from collections import deque


class D:
    """ 데이터 """
    TEST_COUNT: int


class P:

    def __init__(self) -> None:
        D.TEST_COUNT = int(input.readline())

    def run(self) -> None:
        for _ in range(D.TEST_COUNT):
            count = int(input.readline())
            word = deque([])
            for char in input.readline().strip().split():
                if not word:
                    word.append(char)
                    continue
                if ord(word[0]) >= ord(char): word.appendleft(char)
                else: word.append(char)

            print("".join(word))


if __name__ == '__main__':
    # input = open('./13417.txt')
    P = P()
    P.run()