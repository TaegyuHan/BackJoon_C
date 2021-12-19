import math
from sys import stdin as input

class P15610:

    def input_data(self):
        self.a = int(input.readline())

    def result(self):
        print(4*math.sqrt(self.a))


if __name__ == '__main__':
    # input = open('./15610.txt')
    P = P15610()
    P.input_data()
    P.result()