from sys import stdin as input
from math import sqrt

class P3034:

    def input_data(self):
        self.N, self.W, self.H = map(int , input.readline().split())
        self.check_size = max(self.W, self.H, sqrt(self.W**2 + self.H**2))

    def _check_in(self, num):
        if num <= self.check_size:
            print("DA")
        else:
            print("NE")

    def result(self):
        for _ in range(self.N):
            self._check_in(int(input.readline()))


if __name__ == '__main__':
    # input = open('./3034.txt')
    P = P3034()
    P.input_data()
    P.result()