from sys import stdin as input
from math import pi


class P21335:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        answer = (self.N / pi) ** 0.5 * 2 * pi
        print(answer)


if __name__ == '__main__':
    # input = open('./21335.txt')
    P = P21335()
    P.input_data()
    P.result()