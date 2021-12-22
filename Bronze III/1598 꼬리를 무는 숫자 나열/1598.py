from sys import stdin as input
from math import ceil

class P1598:

    def input_data(self):
        self.N1, self.N2 = map(int, input.readline().split())

    def _height(self, num):
        return abs(num - ceil(num / 4) * 4)

    def _width(self, num):
        return ceil(num / 4)

    def result(self):
        answer = 0
        answer += abs(self._height(self.N1) - self._height(self.N2))
        answer += abs(self._width(self.N1) - self._width(self.N2))
        print(answer)


if __name__ == '__main__':
    # input = open('./1598.txt')
    P = P1598()
    P.input_data()
    P.result()