"""
    Solution code for "BaekJoon 자동완성".

    - Problem link: https://www.acmicpc.net/problem/24883
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.alpha = input.readline().strip()

    def run(self) -> None:
        if self.alpha in ["N", "n"]:
            print("Naver D2")
        else:
            print("Naver Whale")


if __name__ == '__main__':
    # input = open('./24883.txt')
    P = P()
    P.run()