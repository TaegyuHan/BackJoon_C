# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.n = int(input.readline())

    def __input_data(self) -> None:
        self.a, self.b, self.c = sorted(map(int, input.readline().split()))

    def __check_triangle(self, i: int) -> None:
        if self.c**2 == self.a**2 + self.b**2:
            print(f"Scenario #{i}:\nyes\n")
        else:
            print(f"Scenario #{i}:\nno\n")

    def result(self) -> None:
        for i in range(1, self.n + 1):
            self.__input_data()
            self.__check_triangle(i)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./7510.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)