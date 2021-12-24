from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.A, self.B = map(int, input.readline().split())
        self.cicken = int(input.readline())

    def result(self) -> None:
        self.__input_data()
        sum_cash = self.A + self.B
        if (cicken_price := self.cicken * 2) > sum_cash:
            print(sum_cash)
        else:
            print(sum_cash - cicken_price)

if __name__ == '__main__':
    # input = open('./14489.txt')
    P = P()
    P.result()