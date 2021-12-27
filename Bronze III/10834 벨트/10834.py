# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self):
        self.M = int(input.readline())

    def __input_data(self) -> None:
        self.a, self.b, self.belt = map(int, input.readline().split())

    def result(self) -> None:
        answer = 1
        direction = 0
        for _ in range(self.M):
            self.__input_data()
            answer *= self.b / self.a
            if self.belt == 1:
                direction += 1

        print(f"{direction % 2} {answer:.0f}")


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./10834.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)