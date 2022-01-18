# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.N = int(input.readline())
        self.P = [-1] + list(map(int, input.readline().split()))
        self.DP = [-1]

    def result(self) -> None:
        for i in range(1, self.N + 1):
            tmp = [self.P[i]] # 번쨰에서 가장 큰거 찾기
            for j in range(1, i // 2 + 1):
                tmp.append(self.DP[i - j] + self.DP[j])

            self.DP.append(max(tmp)) # 가장 큰 거 찾기

        print(self.DP[self.N])



if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./11052.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)