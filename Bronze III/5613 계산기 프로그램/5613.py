# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        return input.readline().rstrip()

    def result(self) -> None:
        formula = ""
        while (symbol := self.__input_data()) != "=":
            formula += symbol
            if symbol.isdigit():
                formula = str(int(eval(formula)))
        print(formula)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./5613.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)