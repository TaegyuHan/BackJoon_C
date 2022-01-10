# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())

    def __input_data(self) -> None:
        self.wines = [int(input.readline()) for _ in range(self.N)]
        self.dp = [0 for _ in range(self.N)]

    def result(self) -> None:
        self.__input_data()
        if self.N == 1: # 와인이 1개인 경우
            self.dp[0] = self.wines[0]
        elif self.N == 2: # 와인이 2개인 경우
            self.dp[1] = sum(self.wines)
        else: # 3개 이상인 경우
            self.dp[0] = self.wines[0]
            self.dp[1] = self.wines[0] + self.wines[1]
            self.dp[2] = max(
                self.dp[1],
                self.wines[2] + self.wines[0],
                self.wines[2] + self.wines[1]
            )
            print(self.dp[2])
        for i in range(3, self.N):
            self.dp[i] = max(
                max(self.wines[i] + self.wines[i -1] + self.dp[i - 3], self.wines[i] + self.dp[i - 2]),
                self.dp[i - 1]
            )
        print(self.dp[self.N - 1])


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    input = open('2156.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)