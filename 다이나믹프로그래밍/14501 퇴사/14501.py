# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.days = [tuple(map(int, input.readline().split()))
                     for _ in range(self.N)]
        self.DP = [0 for _ in range(self.N + 1)]
        self.answer = 0

    def result(self) -> None:
        for i in range(self.N - 1, -1, -1):
            if i + self.days[i][0] > self.N:
                self.DP[i] = self.DP[i + 1]
            else:
                self.DP[i] = max(
                    self.days[i][1] + self.DP[i + self.days[i][0]], # 뒤의 DP랑 더한 것
                    self.DP[i + 1] # 뒤의 손님
                )

        print(self.DP[0])

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./14501.txt')
    P = P()
    P.result()
