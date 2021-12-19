from sys import stdin as input
from math import pi, sqrt

class P20352:

    def input_data(self):
        self.a = int(input.readline())

    def result(self):
        print(sqrt(self.a / pi) * 2 * pi)


if __name__ == '__main__':
    # input = open('./20352.txt')
    P = P20352()
    P.input_data()
    P.result()