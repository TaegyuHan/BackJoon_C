"""
    Solution code for "BaekJoon 절댓값 힙".

    - Problem link: https://www.acmicpc.net/problem/11286
"""
from sys import stdin as input
import heapq
import sys; sys.setrecursionlimit(2500)
# input = open('./11286.txt')


class D:
    """ 데이터 """
    COUNT = 0
    heapq_list = []
    POP = 0


class P:

    def __init__(self) -> None:
        D.COUNT = int(input.readline())

    def run(self) -> None:
        """ 실행 """
        for _ in range(D.COUNT):
            input_num = int(input.readline())
            if input_num == D.POP:
                if D.heapq_list:
                    print(heapq.heappop(D.heapq_list)[1])
                    continue
                print(0)
            else:
                heapq.heappush(D.heapq_list, (abs(input_num), input_num))


if __name__ == '__main__':
    P = P()
    P.run()