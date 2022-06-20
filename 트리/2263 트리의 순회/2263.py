"""
    Solution code for "BaekJoon 트리의 순회".

    - Problem link: https://www.acmicpc.net/problem/2263
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(10**9)
# input = open('./2263.txt')


class D:
    """ 데이터 """
    NODE_COUNT = 0
    in_orders = []
    post_orders = []
    position = []

class P:

    def __init__(self) -> None:
        D.NODE_COUNT = int(input.readline())
        D.in_orders = list(map(int, input.readline().split()))
        D.post_orders = list(map(int, input.readline().split()))

        D.position = [0] * (D.NODE_COUNT + 1)
        for i in range(D.NODE_COUNT):
            D.position[D.in_orders[i]] = i

    def _tree(self, in_start, in_end, post_start, post_end) -> None:
        """ 트리 생성 """
        if in_start > in_end \
            or post_start > post_end:
            return

        parent = D.post_orders[post_end]
        print(parent, end=" ")

        left = D.position[parent] - in_start
        right = in_end - D.position[parent]

        self._tree(
            in_start,
            in_start + left - 1,
            post_start,
            post_start + left - 1,
        )

        self._tree(
            in_end - right + 1,
            in_end,
            post_end - right,
            post_end - 1,
        )

    def run(self) -> None:
        self._tree(0, D.NODE_COUNT - 1, 0, D.NODE_COUNT - 1)


if __name__ == '__main__':
    P = P()
    P.run()