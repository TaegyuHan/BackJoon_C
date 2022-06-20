"""
    Solution code for "BaekJoon 트리".

    - Problem link: https://www.acmicpc.net/problem/4256
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./4256.txt')


class D:
    """ 데이터 """
    TEST_CASE: int

    # 케이스 데이터
    node_count: int
    pre_orders: list[int]
    pre_idx = 0
    in_orders: list[int]

    @classmethod
    def show_data(cls):
        """ 데이터 보여주기 """


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _tree(self, root: int, start: int, end: int):
        """ 트리 만들기 """
        for i in range(start, end):
            if D.in_orders[i] == D.pre_orders[root]:
                self._tree(root + 1, start, i)
                self._tree(root + 1 + i - start, i + 1, end)
                print(D.pre_orders[root], end=" ")

    def _test_run(self):
        """ 테스트 실행 """
        D.node_count = int(input.readline())
        D.pre_orders = list(map(int, input.readline().split()))
        D.in_orders = list(map(int, input.readline().split()))
        self._tree(root=0, start=0, end=D.node_count)
        print()

    def run(self) -> None:
        for _ in range(D.TEST_CASE):
            self._test_run()


if __name__ == '__main__':
    P = P()
    P.run()