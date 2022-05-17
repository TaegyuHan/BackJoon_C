"""
    Solution code for "BaekJoon 카드 놓기".

    - Problem link: https://www.acmicpc.net/problem/18115
"""

from sys import stdin as input
from collections import deque

class P:

    def __init__(self) -> None:
        self._card_count = int(input.readline())
        self._deque = deque([])

    def _type_1(self, num):
        """ 1번 타입 """
        self._deque.appendleft(num)

    def _type_2(self, num):
        """ 2번 타입 """
        one = self._deque.popleft()
        self._deque.appendleft(num)
        self._deque.appendleft(one)

    def _type_3(self, num):
        """ 3번 타입 """
        self._deque.append(num)

    def run(self) -> None:
        for num, cmd in enumerate(reversed(input.readline().split())):
            num += 1
            if cmd == "1": self._type_1(num)
            elif cmd == "2": self._type_2(num)
            elif cmd == "3": self._type_3(num)

        print(*self._deque)


if __name__ == '__main__':
    # input = open('./18115.txt')
    P = P()
    P.run()