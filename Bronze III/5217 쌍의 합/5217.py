# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.TEST_CASE = int(input.readline())

    def __input_data(self) -> None:
        self.number = int(input.readline())

    def __find_pair(self):
        pairs = []
        for i in range(1, self.number // 2 + 1):
            if i == (tmp := self.number - i): continue
            pairs.append(f"{i} {tmp}")
        print(f"Pairs for {self.number}: {', '.join(pairs)}")

    def result(self) -> None:
        for _ in range(self.TEST_CASE):
            self.__input_data()
            self.__find_pair()


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./5217.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)