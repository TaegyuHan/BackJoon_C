"""
    Solution code for "BaekJoon 카드1".

    - Problem link: https://www.acmicpc.net/problem/
"""

from sys import stdin as input
from collections import deque

class P:

    def run(self) -> None:
        num = int(input.readline())
        q = deque([i for i in range(1, num + 1)])
        answer = []
        chage = 0
        while q:
            chage += 1
            if chage % 2:
                answer.append(q.popleft())
                continue
            q.append(q.popleft())

        print(*answer)

if __name__ == '__main__':
    # input = open('./2161.txt')
    P = P()
    P.run()