import math
from sys import stdin as input

class P8710:

    def input_data(self):
        self.k, self.w, self.m = map(int, input.readline().split())

    def result(self):
        break_diff = self.w - self.k
        print(math.ceil(break_diff/self.m))

if __name__ == '__main__':
    # input = open('./8710.txt')
    P = P8710()
    P.input_data()
    P.result()