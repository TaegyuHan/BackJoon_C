# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        tmp = int("0b" + input.readline(), 2)
        print(format(tmp, 'o'))

    def result(self) -> None:
        self.__input_data()

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./1373.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)