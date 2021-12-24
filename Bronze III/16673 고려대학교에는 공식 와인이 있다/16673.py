from sys import stdin as input
from dataclasses import dataclass

class P:

    def input_data(self):
        self.C, self.K, self.P = map(int, input.readline().split())

    def calculation(self, i):
        return self.K * i + self.P * i ** 2

    def result(self):
        print(sum(map(self.calculation, range(1, self.C + 1))))

if __name__ == '__main__':
    # input = open('./16673.txt')
    P = P()
    P.input_data()
    P.result()
