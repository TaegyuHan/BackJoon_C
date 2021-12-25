from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> int:
        self.numerator, self.denominator = map(int, input.readline().split())
        return abs(self.numerator) + abs(self.denominator)


    def result(self) -> None:
        while self.__input_data():
            print(
                self.numerator // self.denominator,
                self.numerator % self.denominator,''
                "/",
                self.denominator
            )

if __name__ == '__main__':
    # input = open('./10474.txt')
    P = P()
    P.result()