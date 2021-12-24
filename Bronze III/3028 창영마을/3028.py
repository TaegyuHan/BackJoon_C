from sys import stdin as input
from dataclasses import dataclass

class P:

    def input_data(self):
        self.cup = [True, False, False]
        self.shuffle = input.readline().rstrip()

    def __A(self):
        self.cup[0], self.cup[1] = self.cup[1], self.cup[0]

    def __B(self):
        self.cup[1], self.cup[2] = self.cup[2], self.cup[1]

    def __C(self):
        self.cup[0], self.cup[2] = self.cup[2], self.cup[0]

    def __check(self, s):
        if s == 'A':
            self.__A()
        elif s == 'B':
            self.__B()
        elif s == 'C':
            self.__C()

    def __answer(self):
        print(self.cup.index(True) + 1)

    def result(self):
        for s in self.shuffle:
            self.__check(s)
        self.__answer()

if __name__ == '__main__':
    # input = open('./3028.txt')
    P = P()
    P.input_data()
    P.result()