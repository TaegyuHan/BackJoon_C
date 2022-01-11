# import time
from operator import mod
from sys import stdin as input
from dataclasses import dataclass

class P:

    def _input_data(self) -> None:
        self.N = int(input.readline())
        self.dp = [0] + [1 for _ in range(1, 10)] # 첫번째

    def _answer(self):
        MOD = 1_000_000_000
        print(sum(self.dp) % MOD)

    def result(self) -> None:
        self._input_data()
        for _ in range(self.N - 1):
            temp = self.dp[:]
            self.dp[0] = temp[1]
            self.dp[9] = temp[8]
            for i in range(1, 9):
                self.dp[i] = temp[i - 1] + temp[i + 1]

        self._answer()

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./10844.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)