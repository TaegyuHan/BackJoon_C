# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def _input_data(self) -> None:
        self._input_number = int(input.readline())
        self.DP = [0, 1]

    def result(self) -> None:
        self._input_data()

        # 들어온 값이 1이 아니면 DP 알고리즘 적용
        if self._input_number != 1:
            for i in range(2, self._input_number + 1):
                self.DP.append(self.DP[i - 1] + self.DP[i - 2])

        print(self.DP[self._input_number])


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./2748.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)