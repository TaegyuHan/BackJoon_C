"""Solution code for "BaekJoon 제곱수의 합".

- Problem link: https://www.acmicpc.net/problem/1699
"""

from sys import stdin as input
from sys import maxsize

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.DP = [0, 1]

    def _DP_RUM(self):
        for index in range(2, self.N + 1):
            # 완전 제곱 가능한 수 찾기
            tmp_min = maxsize
            for num in range(int(index ** 0.5), 0, -1):
                front_index = index - num**2
                tmp_min = min(tmp_min, self.DP[front_index] + 1)
            self.DP.append(tmp_min) # 기존의 값 구해서 넣기

    def result(self) -> None:
        self._DP_RUM()
        print(self.DP[-1])


if __name__ == '__main__':
    input = open('./1699.txt')
    P = P()
    P.result()