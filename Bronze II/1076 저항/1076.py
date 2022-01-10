# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.INPUT_DATA_COUNT = 3
        self.TALBE = {
            "black": ("0", 1),
            "brown": ("1", 10),
            "red": ("2", 100),
            "orange": ("3", 1_000),
            "yellow": ("4", 10_000),
            "green": ("5", 100_000),
            "blue": ("6", 1_000_000),
            "violet": ("7", 10_000_000),
            "grey": ("8", 100_000_000),
            "white": ("9", 1_000_000_000)
        }

    def __input_data(self) -> str:
        return input.readline().rstrip()

    def result(self) -> None:
        answer = ""
        for _ in range(self.INPUT_DATA_COUNT - 1):
            answer += self.TALBE[self.__input_data()][0]

        print(int(answer) * self.TALBE[self.__input_data()][1])

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./1076.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)