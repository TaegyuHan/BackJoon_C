# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())
        self.DP = [1, 2]
        self.MOD = 15_746

    def result(self) -> None:
        for i in range(2, self.N):
            self.DP.append((self.DP[i - 2] + self.DP[i - 1])
                           % self.MOD)
            # 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.

        print(self.DP[self.N - 1])

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./1904.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)