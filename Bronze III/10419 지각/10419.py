# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())

    def __input_data(self):
        self.d = int(input.readline())

    def __calculation(self):
        i = 0
        while True:
            if i + i**2 == self.d:
                print(i)
                break
            elif i + i**2 > self.d:
                print(i - 1)
                break
            i += 1

    def result(self) -> None:
        for _ in range(self.N):
            self.__input_data()
            self.__calculation()


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./10419.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)