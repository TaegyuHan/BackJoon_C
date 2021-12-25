from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.n1, self.n2, self.n3 = map(int, input.readline().split())
        return  abs(self.n1) + abs(self.n2) + abs(self.n3)

    def __check_AP(self) -> int:
        if (self.n3 + self.n1) / 2 == self.n2:
            return self.n2 - self.n1
        else:
            return 0

    def __check_GP(self) -> int:
        if self.n1 * self.n3 == self.n2*self.n2:
            return self.n2 // self.n1
        else:
            return 0

    def result(self) -> None:
        while self.__input_data():
            if tmp := self.__check_AP():
                print("AP", self.n3 + tmp)
            elif tmp := self.__check_GP():
                print("GP", self.n3 * tmp)
                

if __name__ == '__main__':
    # input = open('4880.txt')
    P = P()
    P.result()