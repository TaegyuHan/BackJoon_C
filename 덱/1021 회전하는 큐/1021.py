"""
    Solution code for "BaekJoon 덱".

    - Problem link: https://www.acmicpc.net/problem/1021
"""
from sys import stdin as input
from collections import deque


class P:

    def __init__(self):
        self._queue_num, self._out_count = map(int, input.readline().split())
        self._deque = deque([i for i in range(1, self._queue_num + 1)])
        self._out_numbers = list(map(int, input.readline().split()))
        self._answer = 0

    def _turn_left(self, count):
        """ 왼쪽으로 돌리기 """
        for _ in range(count):
            self._deque.append(self._deque.popleft())

    def _turn_right(self, count):
        """ 오른쪽으로 돌리기 """
        for _ in range(count):
            self._deque.appendleft(self._deque.pop())

    def _find_num(self, num):
        """ 번호 찾기 """
        # 맨앞에서 번호를 찾은 경우
        if self._deque[0] == num:
            return self._deque.popleft()

        # 왼쪽 오른쪽 찾기
        turn_count = len(self._deque)
        for i in range(turn_count):
            if self._deque[i] == num: break

        left, right = i, turn_count - i
        if left <= right: # 왼쪽으로 돌리기
            self._turn_left(left)
        elif left > right:  # 오른쪽으로 돌리기
            self._turn_right(right)
        self._answer += min(left, right)

        if self._deque[0] == num:
            return self._deque.popleft()

    def run(self) -> None:
        self._answer = 0
        for num in self._out_numbers:
            self._find_num(num)
        print(self._answer)


if __name__ == '__main__':
    # input = open('./1021.txt')
    P = P()
    P.run()