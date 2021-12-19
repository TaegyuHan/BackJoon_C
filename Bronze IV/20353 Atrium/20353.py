import math
from sys import stdin as input

class P20353:

    def input_data(self):
        self.A = int(input.readline())

    def result(self):
        print(4 * math.sqrt(self.A))

if __name__ == '__main__':
    # input = open('./20353.txt')
    P = P20353()
    P.input_data()
    P.result()