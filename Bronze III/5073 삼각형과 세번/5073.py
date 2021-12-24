from sys import stdin as input
from dataclasses import dataclass


class P:

    @staticmethod
    def __input_data():
        return tuple(map(int, input.readline().split()))

    @staticmethod
    def __check_triangle(s1, s2, s3):
        max_s = max(s1, s2, s3)
        other_s_sum = sum((s1, s2, s3)) - max_s
        if other_s_sum > max_s:
            return True
        else:
            return False

    @staticmethod
    def __check_triangle_shape(s1, s2, s3):
        if not P.__check_triangle(s1, s2, s3):
            print("Invalid")
        elif s1 == s2 and s2 == s3 and  s1 == s3:
            print("Equilateral")
        elif s1 == s2 or s2 == s3 or  s1 == s3:
            print("Isosceles")
        else:
            print("Scalene")

    def result(self):
        while sum(triangle := P.__input_data()):
            s1, s2, s3 = triangle
            self.__check_triangle_shape(s1, s2, s3)


if __name__ == '__main__':
    # input = open('./5073.txt')
    P = P()
    P.result()