# import time
from sys import stdin as input
from math import ceil
from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())

    def __star_one(self):
        print("*")

    def __star_up(self):
        return f"{'* ' * ceil(self.N / 2)}\n"

    def __star_down(self):
        return f"{' *' * ceil(self.N // 2)}\n"

    def __star(self):
        star = self.__star_up()
        star += self.__star_down()
        return star

    def result(self) -> None:
        answer = ""
        if self.N  == 1:
            self.__star_one()
        else:
            answer += self.__star() * self.N
            print(answer)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./10996.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)