"""
    Solution code for "BaekJoon 소인수 분해".

    - Problem link: https://www.acmicpc.net/problem/11653
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./11653.txt')

class P:

    def run(self) -> None:
        n = int(input.readline())
        div_number = 2
        while n != 1:
            if n % div_number == 0:
                print(div_number)
                n /= div_number
            else:
                div_number += 1

if __name__ == '__main__':
    P = P()
    P.run()