"""
    Solution code for "BaekJoon 암기왕".

    - Problem link: https://www.acmicpc.net/problem/2776
"""

from sys import stdin as input
from collections import defaultdict

class D:
    """ 데이터 """
    TEST_CASE: int

class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _input_data(self):
        """ 데이터 받기 """
        self._input_count = int(input.readline())
        self._nums = map(int, input.readline().split())
        self._test_count = int(input.readline())
        self._test_nums = map(int, input.readline().split())

    def _check(self):
        """ 데이터 확인하기 """
        num_dict = defaultdict(int)
        for key in self._nums:
            num_dict[key] += 1

        for check in self._test_nums:
            if check in num_dict.keys(): print(1)
            else: print(0)

    def run(self) -> None:
        for _ in range(D.TEST_CASE):
            self._input_data()
            self._check()


if __name__ == '__main__':
    # input = open('./2776.txt')
    P = P()
    P.run()