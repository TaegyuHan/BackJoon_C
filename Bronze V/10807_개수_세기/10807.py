"""
    Solution code for "BaekJoon 개수 세기".

    - Problem link: https://www.acmicpc.net/problem10807
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
from collections import defaultdict
#  input = open('./10807.txt')


class D:
    """ 데이터 """
    N: int
    num_dict = defaultdict(int)


class P:

    def __init__(self) -> None:
        D.N = int(input.readline())
        for num in map(int, input.readline().split()):
            D.num_dict[num] += 1

        key = int(input.readline())
        print(D.num_dict[key])

    def run(self) -> None:
        pass


if __name__ == '__main__':
    P = P()
    P.run()