# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())

    def __mid(self) -> str:
        side = ("@" * self.N)
        mid = (" " * 3 * self.N)
        return f'{side}{mid}{side}\n' * 3 * self.N

    def __bottom(self) -> str:
        return f'{"@" * 5 * self.N}\n' * self.N

    def __top(self) -> str:
        return f'{"@" * 5 * self.N}\n' * self.N

    def result(self) -> None:
        answer = ""
        answer += self.__top()
        answer += self.__mid()
        answer += self.__bottom()
        print(answer)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./23806.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)