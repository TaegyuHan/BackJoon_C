# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.TEST_TIME = int(input.readline())
        self.tmp = [int(input.readline())]

    def __input_data(self) -> int:
        self.in_car, self.out_car = map(int, input.readline().split())
        return self.in_car - self.out_car

    def result(self) -> None:
        answer = 0
        for i in range(self.TEST_TIME):
            value = self.tmp[i] + self.__input_data()

            if value < 0:
                print(0)
                return
            self.tmp.append(value)

        print(max(self.tmp))


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./5612.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)