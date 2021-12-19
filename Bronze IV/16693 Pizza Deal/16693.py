from math import pi
from sys import stdin as input

class P16693:

    def input_data(self):
        self.A1, self.P1 = map(int, input.readline().split())
        self.R1, self.P2 = map(int, input.readline().split())

    def result(self):
        if (self.P1 / self.A1) < (self.P2 / (self.R1 ** 2 * pi)):
            print("Slice of pizza")
        else:
            print("Whole pizza")

if __name__ == '__main__':
    # input = open('./16693.txt')
    P = P16693()
    P.input_data()
    P.result()