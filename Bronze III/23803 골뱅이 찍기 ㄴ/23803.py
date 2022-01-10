# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())

    def __top(self) -> None:
        return f"{'@' * self.N}\n" * self.N * 4

    def __mid(self) -> None:
        return f"{'@' * self.N * 5}\n" * self.N

    def result(self) -> None:
        answer = ""
        answer += self.__top()
        answer += self.__mid()
        print(answer)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./23803.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)