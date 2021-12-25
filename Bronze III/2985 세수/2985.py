from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.N1, self.N2, self.N3 = input.readline().split()

    @staticmethod
    def __calculation(num1: str, num2: str, num3: str, symbol: str) -> bool:
        if eval(tmp := "".join((num1, symbol, num2))) == int(num3):
            print(tmp + '=' + num3)
            return False
        elif eval(tmp := "".join((num2, symbol, num3))) == int(num1):
            print(num1 + '=' +tmp)
            return False

        return True

    def result(self) -> None:
        self.__input_data()
        for symbol in ["+", "-", "*", "/"]:
            if not self.__calculation(self.N1, self.N2, self.N3, symbol):
                break


if __name__ == '__main__':
    # input = open('./2985.txt')
    P = P()
    P.result()