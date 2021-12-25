from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.STORE_COUNT = int(input.readline())
        self.stores = map(int, input.readline().split())
        self.milks = [0, 1, 2]
        self.current_milk = 0

    def __next_milk(self) -> None:
        self.current_milk += 1
        if self.current_milk > 2:
            self.current_milk = 0

    def result(self) -> None:
        answer = 0
        self.__input_data()
        for store in self.stores:
            if self.current_milk == store:
                answer += 1
                self.__next_milk()
        print(answer)


if __name__ == '__main__':
    # input = open('./14720.txt')
    P = P()
    P.result()