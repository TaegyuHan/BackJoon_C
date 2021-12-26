# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.helmet_count, self.vest_count = map(int, input.readline().split())
        self.helmet_max = max(map(int, input.readline().split()))
        self.vest_max = max(map(int, input.readline().split()))

    def result(self) -> None:
        self.__input_data()
        print(self.helmet_max + self.vest_max)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./15781.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)