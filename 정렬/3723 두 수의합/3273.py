"""
    Solution code for "BaekJoon 두 수의 합".

    - Problem link: https://www.acmicpc.net/problem/3273
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.number = [False for _ in range(2_000_001)]
        for i in map(int, input.readline().split()):
            self.number[i] = True
        self.x = int(input.readline())

    def run(self) -> None:
        count = 0
        for i in range(1, 2_000_001):
            if self.number[i] and self.number[self.x - i]:
                count += 1
        print(count//2)

if __name__ == '__main__':
    # input = open('./3273.txt')
    P = P()
    P.run()