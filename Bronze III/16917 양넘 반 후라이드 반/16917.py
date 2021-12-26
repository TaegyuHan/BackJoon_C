# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.A, self.B, self.C, self.X, self.Y = \
            map(int, input.readline().split())

    @staticmethod
    def __price_comparison(price1: int, price2: int) -> int:
        if price1 > price2:
            return 2 # 반반으로 구매
        else:
            return 1 # 1마리로 구매

    def __buy_one(self) -> int:
        return (self.A * self.X) + (self.B * self.Y)

    def __buy_half(self) -> int:
        d = min(self.X, self.Y)
        return (2 * self.C * d) + \
               (min(2 * self.C, self.A) * max(0, self.X - d)) + \
               (min(2 * self.C, self.B) * max(0, self.Y - d))

    def result(self) -> None:
        self.__input_data()
        purchase = self.__price_comparison(self.A + self.B, self.C * 2)

        if purchase == 1:
            print(self.__buy_one())
        else:
            print(self.__buy_half())


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./16917.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)