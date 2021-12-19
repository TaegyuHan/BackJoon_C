from math import ceil
from sys import stdin as input

class P16785:

    def input_data(self):
        self.A, self.B, self.C = map(int, input.readline().split())
        self.D = 7 * self.A + self.B

    def result(self):
        print(self.C // self.D * 7 + min(ceil(self.C % self.D / self.A), 7))

if __name__ == '__main__':
    # input = open('./16785.txt')
    P = P16785()
    P.input_data()
    P.result()
