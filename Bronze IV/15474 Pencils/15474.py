import math
from sys import stdin as input

class P15474:

    def input_data(self):
        self.N, self.A, self.B, self.C, self.D = map(int, input.readline().split())

    def result(self):
        cash1 = math.ceil(self.N / self.A) * self.B
        cash2 = math.ceil(self.N / self.C) * self.D
        print(min(cash1, cash2))


if __name__ == '__main__':
    # input = open('./15474.txt')
    P = P15474()
    P.input_data()
    P.result()