"""
    Solution code for "BaekJoon AC".

    - Problem link: https://www.acmicpc.net/problem/5430
"""
from sys import stdin as input
from collections import deque


class D:
    TEST_CASE: int


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _input_data(self):
        """ 테이스 케이스 데이터 받기 """
        self._cmd = input.readline().strip()
        self._count = int(input.readline())
        self._nums = deque(list(input.readline().strip()[1:-1].split(",")))

    def _case(self):
        """  """
        reverse = False
        for cmd in self._cmd:
            if cmd == "R": reverse = not reverse
            elif cmd == "D":
                if not self._nums or self._nums[0] == "":
                    print("error")
                    return
                if reverse:
                    self._nums.pop()
                else:
                    self._nums.popleft()
        if reverse:
            print(f"[{','.join(reversed(self._nums))}]")
        else:
            print(f"[{','.join(self._nums)}]")

    def test(self) -> None:
        for _ in range(D.TEST_CASE):
            self._input_data()
            self._case()


if __name__ == '__main__':
    # input = open('./5430.txt')
    P = P()
    P.test()