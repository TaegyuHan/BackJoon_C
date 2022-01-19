import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.MAX_N = 1_000_000 + 1
        self.TEST_COUNT = int(input.readline())
        self.DP = [0 for _ in range(self.MAX_N + 1)] # 1로 초기화

    def _input_data(self) -> None:
        self.N = int(input.readline())

    def _make_dp(self) -> None:
        for i in range(1, self.MAX_N):
            for j in range(i, self.MAX_N, i):
                self.DP[j] += i
            self.DP[i] += self.DP[i - 1]

    def result(self) -> None:
        self._make_dp()
        for _ in range(self.TEST_COUNT):
            self._input_data()
            print(self.DP[self.N])


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./17425.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)