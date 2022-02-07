# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.num = int(input.readline())

    def result(self) -> None:
        if self.num < 10:
            print(self.num)
        elif self.num < 100:
            print(9 + (self.num - 9) * 2)
        elif self.num < 1_000:
            print(189 + (self.num - 99) * 3)
        elif self.num < 10_000:
            print(2889 + (self.num - 999) * 4)
        elif self.num < 100_000:
            print(38889 + (self.num - 9999) * 5)
        elif self.num < 1_000_000:
            print(488889 + (self.num - 99999) * 6)
        elif self.num < 10_000_000:
            print(5888889 + (self.num - 999999) * 7)
        elif self.num < 100_000_000:
            print(68888889 + (self.num - 9999999) * 8)
        elif self.num < 1_000_000_000:
            print(788888889 + (self.num - 99999999) * 9)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    input = open('./1748.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)