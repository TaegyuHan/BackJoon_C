from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.N = int(input.readline())

    def result(self) -> None:
        self.__input_data()
        answer = 0
        for i in range(1, self.N + 1):
            number = str(i)
            answer += number.count("3")
            answer += number.count("6")
            answer += number.count("9")

        print(answer)


if __name__ == '__main__':
    # input = open('./17614.txt')
    P = P()
    P.result()