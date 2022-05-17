"""
    Solution code for "BaekJoon Router".

    - Problem link: https://www.acmicpc.net/problem/15828
"""

from sys import stdin as input
from collections import deque

class S:
    """ 상태 """
    DONE = "0"
    BREAK = "-1"


class P:

    def run(self) -> None:
        buffer_size = int(input.readline())
        q = deque([])
        while True:
            packet = input.readline().strip()
            if packet == S.BREAK: break
            elif packet == S.DONE: q.popleft()
            elif len(q) < buffer_size: q.append(packet)

        if q:
            print(*q)
        else:
            print("empty")


if __name__ == '__main__':
    # input = open('./15828.txt')
    P = P()
    P.run()