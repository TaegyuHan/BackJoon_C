"""Solution code for "BaekJoon 부등호".

- Problem link: https://www.acmicpc.net/problem/2529
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.SIGN_COUNT = int(input.readline())
        self._signs = input.readline().split()

    def _check_possible(self, num1: int, num2: int, sign: str) -> bool:
        if sign == "<":
            return num1 < num2
        if sign == ">":
            return num1 > num2

    def _backtracking(self, index: int, answer: str) -> None:
        if index == self.SIGN_COUNT + 1:
            if not len(self.min):
                self.min = answer
                return
            else:
                self.max = answer
                return

        for i in range(0, 10):
            if self._check_number[i] == False:
                if index == 0:
                    self._check_number[i] = True
                    self._backtracking(index + 1, answer + str(i))
                    self._check_number[i] = False
                elif self._check_possible(answer[-1], str(i), self._signs[index - 1]):
                    self._check_number[i] = True
                    self._backtracking(index + 1, answer + str(i))
                    self._check_number[i] = False

    def result(self) -> None:
        self._check_number = [False for _ in range(10)]
        self.min, self.max = "", ""
        self._backtracking(index=0, answer="")
        print(self.max)
        print(self.min)


if __name__ == '__main__':
    # input = open('./2529.txt')
    P = P()
    P.result()