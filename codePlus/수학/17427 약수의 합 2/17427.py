# import math
import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())

    def result(self) -> None:
        answer = 0
        for i in range(1, self.N + 1):
            answer += i * (self.N // i)
        print(answer)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./17427.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)