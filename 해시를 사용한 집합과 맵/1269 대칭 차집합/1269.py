"""
    Solution code for "BaekJoon 대칭 차집합".

    - Problem link: https://www.acmicpc.net/problem/1269
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self._A, self._B = map(int, input.readline().split())
        self._Aset = set(map(int, input.readline().split()))
        self._Bset = set(map(int, input.readline().split()))

    def run(self) -> None:
        print(len(self._Aset ^ self._Bset))

if __name__ == '__main__':
    # input = open('./1269.txt')
    P = P()
    P.run()