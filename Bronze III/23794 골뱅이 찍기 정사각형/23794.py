# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())

    def __top(self) -> None:
        return f"@{'@' * self.N}@\n"

    def __mid(self) -> None:
        return f"@{' ' * self.N}@\n" * self.N

    def __bot(self) -> None:
        return f"@{'@' * self.N}@\n"

    def result(self) -> None:
        answer = ""
        answer += self.__top()
        answer += self.__mid()
        answer += self.__bot()
        print(answer)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./23794.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)