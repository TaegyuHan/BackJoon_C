from sys import stdin as input
from dataclasses import dataclass

class P:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    def result(self):
        for _ in range(self.TEST_CASE):
            answer = 0
            N, K = map(int, input.readline().split())
            candys = map(int, input.readline().split())
            for candy in candys:
                answer += candy // K
            print(answer)


if __name__ == '__main__':
    # input = open('./9550.txt')
    P = P()
    P.input_data()
    P.result()