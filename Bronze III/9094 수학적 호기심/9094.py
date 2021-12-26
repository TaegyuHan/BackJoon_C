from sys import stdin as input
from itertools import combinations
from dataclasses import dataclass

class P:

    def __init__(self):
        self.TEST_CASE = int(input.readline())

    def __input_data(self) -> None:
        self.n, self.m = map(int, input.readline().split())

    def __calculation_func(self) -> int:
        return sum((a ** 2 + b ** 2 + self.m) % (a * b) == 0 for a, b in combinations(range(1, self.n), 2))

    def result(self) -> None:
        for _ in range(self.TEST_CASE):
            self.__input_data()
            print(self.__calculation_func())


if __name__ == '__main__':
    # input = open('./9094.txt')
    P = P()
    P.result()