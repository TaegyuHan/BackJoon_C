from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.before = float(input.readline())
        self.STOP_NUMBER = 999.0

    def __input_data(self) -> float:
        self.after = float(input.readline())
        return self.after

    def result(self) -> None:
        while self.__input_data() != self.STOP_NUMBER:
            print(f"{self.after - self.before:.2f}")
            self.before = self.after


if __name__ == '__main__':
    # input = open('./4766.txt')
    P = P()
    P.result()