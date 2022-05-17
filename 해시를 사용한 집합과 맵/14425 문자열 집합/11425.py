"""
    Solution code for "BaekJoon 문자열 집합".

    - Problem link: https://www.acmicpc.net/problem/14425
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self._N, self._M = map(int, input.readline().split())
        self._check = set(input.readline().strip() for _ in range(self._N))

    def run(self) -> None:
        answer = 0
        for _ in range(self._M):
            if input.readline().strip() in self._check:
                answer += 1
        print(answer)


if __name__ == '__main__':
    # input = open('./11425.txt')
    P = P()
    P.run()