# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.number_list = sorted(map(int, input.readline().split()))
        self.check_number_list = [False for _ in range(self.N)]
        self.answer = [0 for _ in range(self.M)]

    def _backtracking(self, count: int) -> None:
        if count == self.M:
            print(" ".join(map(str, self.answer)))
            return

        for i in range(self.N):
            if self.check_number_list[i] == False:
                self.answer[count] = self.number_list[i]
                self.check_number_list[i] = True
                self._backtracking(count + 1)
                self.check_number_list[i] = False

    def result(self) -> None:
        self._backtracking(count=0)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./15654.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)