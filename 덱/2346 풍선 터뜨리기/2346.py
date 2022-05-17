"""
    Solution code for "BaekJoon 풍선 터뜨리기".

    - Problem link: https://www.acmicpc.net/problem/2346
"""

from sys import stdin as input
from collections import deque


class P:

    def __init__(self) -> None:
        self._count = int(input.readline())
        self._deque = deque([])
        self._paper = list(map(int, input.readline().split()))
        for i in range(1, self._count + 1):
            self._deque.append((i, self._paper[i - 1]))
        self._answer = []

    def _move_left(self, count):
        """ 왼쪽으로 이동 """
        for _ in range(abs(count)):
            self._deque.append(self._deque.popleft())

    def _move_right(self, count):
        """ 오른쪽으로 이동 """
        for _ in range(abs(count)):
            self._deque.appendleft(self._deque.pop())

    def run(self) -> None:
        while self._deque:
            num, move_count = self._deque.popleft()
            self._answer.append(num)
            if not self._deque: break
            if move_count > 0:
                self._move_left(move_count - 1)
            elif move_count < 0:
                self._move_right(move_count)

        print(*self._answer)


if __name__ == '__main__':
    # input = open('./2346.txt')
    P = P()
    P.run()