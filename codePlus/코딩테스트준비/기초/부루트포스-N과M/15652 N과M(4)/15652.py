# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.answer = [0 for _ in range(self.M)]

    def _backtraking(self, count: int):
        if count == self.M:
            print(" ".join(map(str, self.answer)))
            return

        for i in range(self.N):
            if count > 0 and (i + 1) < self.answer[count - 1]:
                continue
            self.answer[count] = i + 1
            self._backtraking(count + 1)

    def result(self) -> None:
        self._backtraking(0)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./15652.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)