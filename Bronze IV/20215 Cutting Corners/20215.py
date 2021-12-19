import math
from sys import stdin as input

class P20215:

    def input_data(self):
        self.w, self.h = map(int, input.readline().split())

    def result(self):
        rectangle_cut = self.w + self.h
        diagonal_cut = math.sqrt(self.w*self.w + self.h*self.h)
        print(f"{round(rectangle_cut - diagonal_cut, 9)}")

if __name__ == '__main__':
    # input = open('./20215.txt')
    P = P20215()
    P.input_data()
    P.result()