# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        return input.readline()

    @staticmethod
    def __check(text: str):
        low = 0
        up = 0
        num = 0
        empty = 0

        for s in text:
            if s.islower():
                low += 1
            elif s.isupper():
                up += 1
            elif s.isnumeric():
                num += 1
            elif s == ' ':
                empty += 1
        print(low, up, num , empty)

    def result(self) -> None:
        while text := self.__input_data():
            self.__check(text)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./10820.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)