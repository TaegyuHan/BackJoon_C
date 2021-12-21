from math import ceil
from sys import stdin as input

class P8674:

    def input_data(self):
        self.a, self.b = map(int, input.readline().split())

    def result(self):
        w1 = ceil(self.a/2)
        w2 = self.a - ceil(self.a/2)

        h1 = ceil(self.b/2)
        h2 = self.b - ceil(self.b/2)

        div_w = w1 * self.b - w2 * self.b
        div_h = self.a * h1 - self.a * h2
        print(min(div_w, div_h))


if __name__ == '__main__':
    # input = open('./86774.txt')
    P = P8674()
    P.input_data()
    P.result()