# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def _input_data(self) -> None:
        self.N = int(input.readline())
        self.DP = [1, 1]

    def result(self) -> None:
        self._input_data()
        for i in range(2, self.N):
            self.DP.append(self.DP[i - 2] + self.DP[i - 1])

        print(self.DP[self.N - 1])

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./2193.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)