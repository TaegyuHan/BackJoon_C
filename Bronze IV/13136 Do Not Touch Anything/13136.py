import math
from sys import stdin as input

class P13136:

    def input_data(self):
        self.R, self.C, self.N = map(int, input.readline().split())

    def result(self):
        print(math.ceil(self.R / self.N) * math.ceil(self.C / self.N))


if __name__ == '__main__':
    # input = open('./13136.txt')
    P = P13136()
    P.input_data()
    P.result()