# import time
from sys import stdin as input
# from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.TEST_CASE = int(input.readline())
        self.M, self.N, self.x, self.y = 0, 0, 0, 0

    def _input_data(self):
        self.M, self.N, self.x, self.y = map(int, input.readline().split())

    def result(self) -> None:
        for _ in range(self.TEST_CASE):
            self._input_data()
            no_answer = True
            while self.x <= self.M*self.N:
                if (self.x - self.y) % self.N == 0:
                    print(self.x)
                    no_answer = False
                    break
                self.x += self.M

            if no_answer:
                print(-1)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./6064.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)