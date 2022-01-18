# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.T = int(input.readline())

    def _input_date(self) -> None:
        self.n = int(input.readline())
        self.sticker = [list(map(int, input.readline().split()))
                        for _ in range(2)]

    def _max_point(self) -> None:
        if self.n == 1:
            print(max(
                self.sticker[0][0],
                self.sticker[1][0]
            ))
            return
        if self.n == 2:
            print(max(
                self.sticker[0][0] + self.sticker[1][1],
                self.sticker[0][1] + self.sticker[1][0]
            ))
            return
        else:
            # 1, 2가 아니면
            self.sticker[1][1] += self.sticker[0][0]
            self.sticker[0][1] += self.sticker[1][0]

            for i in range(2, self.n):
                self.sticker[0][i] += max(self.sticker[1][i - 2], self.sticker[1][i - 1])
                self.sticker[1][i] += max(self.sticker[0][i - 2], self.sticker[0][i - 1])
                
            print(max(
                self.sticker[0][-1],
                self.sticker[1][-1]
            )) # 정답


    def result(self) -> None:
        for _ in range(self.T):
            self._input_date()
            self._max_point()

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./9465.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)