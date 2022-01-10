# import time
from sys import stdin as input
from math import ceil
# from dataclasses import dataclass

class P:

    def __init__(self):
        self.TEST_ROOM_COUNT = int(input.readline())
        self.TEST_ROOMS = map(int, input.readline().split())
        self.B, self.C = map(int, input.readline().split())

    def result(self) -> None:
        answer = 0
        for people in self.TEST_ROOMS:
            answer += 1
            if people - self.B > 0:
                answer += ceil((people - self.B) / self.C)
        print(answer)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./13458.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)