"""
    Solution code for "BaekJoon 용액".

    - Problem link: https://www.acmicpc.net/problem/2467
"""
import sys
from sys import stdin as input


class D:
    """ 데이터 """
    SOLUTION: int
    SOLUTIONS: list[int]
    diff: int
    answer_a: int
    answer_b: int

class S:
    MAX = sys.maxsize

class N:
    """ 다음 포인터 """
    MOVE = [
        (0, 0),
        (1, 0),
        (0, -1),
        (1, -1)
    ]


class PT:
    """ Pointer 포인터 """
    front: int
    back: int


class P:

    def __init__(self) -> None:
        D.SOLUTION = int(input.readline())
        D.SOLUTIONS = list(map(int, input.readline().split()))
        self._init_pointer()

    def _init_pointer(self):
        """ 포인터 초기화 """
        PT.front = 0
        PT.back = D.SOLUTION - 1

    def run(self) -> None:
        """ 프린트 """
        while PT.front < PT.back:
            diff = D.SOLUTIONS[PT.front] + D.SOLUTIONS[PT.back]

            if abs(diff) < S.MAX:
                D.answer_a = PT.front
                D.answer_b = PT.back
                S.MAX = abs(diff)

            if diff > 0:
                PT.back -= 1
            elif diff < 0:
                PT.front += 1
            else:
                break

        print(D.SOLUTIONS[D.answer_a], D.SOLUTIONS[D.answer_b])

if __name__ == '__main__':
    # input = open('./2467.txt')
    P = P()
    P.run()