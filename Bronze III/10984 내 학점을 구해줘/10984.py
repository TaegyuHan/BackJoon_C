from sys import stdin as input
from math import ceil

class P10984:

    def input_data(self):
        self.TEST_SEMESTER = int(input.readline())

    def result(self):
        for _ in range(self.TEST_SEMESTER):
            self.TEST_COUNT = int(input.readline())
            sum_point, sum_gpa = 0, 0
            for _ in range(self.TEST_COUNT):
                point, gpa = map(float, input.readline().split())
                sum_gpa += point * gpa
                sum_point += point

            if ceil(sum_gpa) == 0:
                print(ceil(sum_point), 0.0)
            else:
                print(ceil(sum_point), round(sum_gpa / ceil(sum_point), 1))


if __name__ == '__main__':
    # input = open('./10984.txt')
    P = P10984()
    P.input_data()
    P.result()