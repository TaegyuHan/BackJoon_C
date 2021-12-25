from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.N = int(input.readline())

    def __even_number(self) -> None:
        self.N = self.N // 2

    def __odd_number(self) -> None:
        self.N = 3 * self.N + 1

    def result(self) -> None:
        self.__input_data()
        answer = 1
        while self.N != 1:
            answer += 1
            if self.N % 2 == 0:
                self.__even_number()
            else:
                self.__odd_number()

        print(answer)


if __name__ == '__main__':
    # input = open('./14920.txt')
    P = P()
    P.result()