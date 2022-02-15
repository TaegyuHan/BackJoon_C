"""Solution code for "BaekJoon 로또"

- Problem link: https://www.acmicpc.net/problem/6603
"""

from sys import stdin as input
from itertools import combinations

class P:

    def _input_data(self) -> None:
        self.number_list = list(map(int, input.readline().split()))

    def result(self) -> None:
        while True:
            self._input_data()

            tmp_list = self.number_list[1:]

            for numbers in combinations(tmp_list, 6):
                print(*numbers)

            if self.number_list[0] == 0:
                return
            print()


if __name__ == '__main__':
    # input = open('./6603.txt')
    P = P()
    P.result()