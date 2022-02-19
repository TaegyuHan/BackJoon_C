"""Solution code for "BaekJoon 오르막 수".

- Problem link: https://www.acmicpc.net/problem/11057
"""
import sys
from sys import stdin as input
sys.setrecursionlimit(10_000)


class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.MOD = 10_007
        self.save = {}

    def _DP(self, index: int, back_number: int):
        if index == self.N:
            return 1

        if f"{index},{back_number}" in self.save.keys():
            return self.save[f"{index},{back_number}"]

        tmp_sum = 0
        for i in range(0, 10):
            if i < back_number: continue
            tmp_sum += self._DP(index + 1, i)
        self.save[f"{index},{back_number}"] = tmp_sum
        return tmp_sum

    def result(self) -> None:
        asnwer = self._DP(index=0, back_number=0)
        print(asnwer % self.MOD)

if __name__ == '__main__':
    # input = open('./11057.txt')
    P = P()
    P.result()