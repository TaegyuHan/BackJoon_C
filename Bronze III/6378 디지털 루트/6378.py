from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        return input.readline().rstrip()

    def result(self) -> None:
        while (num := self.__input_data()) != '0':
            while len(num) != 1:
                num = str(sum(map(int, list(num))))
            print(num)


if __name__ == '__main__':
    # input = open('./6378.txt')
    P = P()
    P.result()