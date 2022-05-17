"""
    Solution code for "BaekJoon 반전 요세푸스".

    - Problem link: https://www.acmicpc.net/problem/20301
"""
from sys import stdin as input
from collections import deque


class P:

    def __init__(self) -> None:
        self._N, self._K, self._M = map(int, input.readline().split())
        self._deque = deque([i for i in range(1, self._N + 1)])
        self._init_start()

    def _init_start(self):
        """ 시작 값 초기화 """
        while True:
            if self._deque[0] == self._K: break
            self._deque.append(self._deque.popleft())

    def _move_left(self):
        """ 왼쪽으로 이동 """
        for _ in range(self._K):
            self._deque.appendleft(self._deque.pop())

    def _move_right(self):
        """ 오른쪽으로 이동 """
        for _ in range(self._K - 1):
            self._deque.append(self._deque.popleft())

    def run(self) -> None:
        move_count = 0
        turn = True
        while self._deque:
            move_count += 1
            print(self._deque.popleft())
            if not self._deque: break

            if move_count == self._M:
                move_count = 0
                turn = not turn

            if turn: self._move_right()
            else: self._move_left()


if __name__ == '__main__':
    # input = open('./20301.txt')
    P = P()
    P.run()