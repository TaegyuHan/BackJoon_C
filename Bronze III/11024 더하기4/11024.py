# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())

    def result(self) -> None:
        for _ in range(self.N):
            print(sum(map(int, input.readline().split())))

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./11024.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)