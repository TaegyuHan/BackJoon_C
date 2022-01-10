import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.F = int(input.readline())

    def result(self) -> None:
        front_number = self.N // 100 * 100
        for i in range(0, 100):
            if (tmp := front_number + i) % self.F == 0:
                print(f"{i:02d}")
                break

if __name__ == '__main__':
    start = time.time()  # 시작 시간 저장
    input = open('./1075.txt')
    P = P()
    P.result()
    print("time :", time.time() - start)