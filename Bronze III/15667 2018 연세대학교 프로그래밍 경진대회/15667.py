from sys import stdin as input
from math import sqrt
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.N = int(input.readline())

    def result(self) -> None:
        self.__input_data()
        print(int(sqrt(self.N)))


if __name__ == '__main__':
    # input = open('./15667.txt')
    P = P()
    P.result()