"""
    Solution code for "BaekJoon 큐 2".

    - Problem link: https://www.acmicpc.net/problem/18258
"""

from sys import stdin as input
from collections import deque

class S:
    """ 상태 """
    PUSH = 2

class Queue:
    """ 큐 자료구조 """

    def __init__(self):
        self._data = deque([])

    def push(self, data):
        """ 데이터 넣기 """
        self._data.append(data)

    def pop(self):
        """ 데이터 뽑기 """
        if len(self._data):
            return self._data.popleft()
        return -1

    def size(self):
        """ 데이터 크기 """
        return len(self._data)

    def empty(self):
        """ 비어 있는지 확인하기 """
        if len(self._data):
            return 0
        return 1

    def front(self):
        """ 큐의 앞의 데이터 """
        if len(self._data):
            return self._data[0]
        return -1

    def back(self):
        """ 큐의 뒤의 데이터 """
        if len(self._data):
            return self._data[-1]
        return -1

class P:

    def run(self) -> None:
        q = Queue()
        data_count = int(input.readline())
        for _ in range(data_count):
            cmd = input.readline().split()
            if len(cmd) == S.PUSH:
                q.push(cmd[1])
                continue

            cmd = cmd[0]
            if cmd == "front": print(q.front())
            elif cmd == "back": print(q.back())
            elif cmd == "size": print(q.size())
            elif cmd == "pop": print(q.pop())
            elif cmd == "empty": print(q.empty())


if __name__ == '__main__':
    # input = open('./18258.txt')
    P = P()
    P.run()