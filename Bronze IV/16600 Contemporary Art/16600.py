from sys import stdin as input
from math import sqrt

class P16600:

    def input_data(self):
        self.a = int(input.readline())

    def result(self):
        print(4 * sqrt(self.a))

if __name__ == '__main__':
    # input = open('./16600.txt')
    P = P16600()
    P.input_data()
    P.result()