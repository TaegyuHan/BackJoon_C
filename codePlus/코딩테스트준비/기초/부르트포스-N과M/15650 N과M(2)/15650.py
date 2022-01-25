import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.check_number_list = [False for i in range(self.N)]
        self.answer = [0 for _ in range(self.M)]

    def _backtracking(self, count: int) -> None:
        if count == self.M:
            print(" ".join(map(str, self.answer)))
            return

        for i in range(self.N):
            if self.check_number_list[i] == False:
                # 뒤에수보다 작으면 pass
                if count > 0 and self.answer[count - 1] > i + 1:
                    continue
                self.answer[count] = i + 1
                self.check_number_list[i] = True
                self._backtracking(count + 1)
                self.check_number_list[i] = False

    def result(self) -> None:
        self._backtracking(0)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('15650.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)