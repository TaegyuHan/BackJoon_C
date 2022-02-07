"""Solution code for "BaekJoon 맞춰봐".

- Problem link: https://www.acmicpc.net/problem/1248
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.arr = list(input.readline())
        self.S = [[0 for _ in range(self.N)]  for _ in range(self.N)]

    def _check(self, index: int)  -> bool:
        hap = 0
        for i in range(index, -1, -1):
            hap += self.answer[i]
            if hap == 0 and self.S[i][index] != 0:
                return False
            elif hap == 0 and self.S[i][index] >= 0:
                return False
            elif hap == 0 and self.S[i][index] <= 0:
                return False
        return True

    def _backtracking(self, index: int) -> bool:
        if index == self.N:
            return True
        if self.S[index][index] == 0:
            self.answer[index] = 0
            return self._backtracking(index + 1)
        for i in range(1, 11):
            self.answer[index] = self.S[index][index] * i
            if self._check(index) and self._backtracking(index + 1):
                return True
        return False

    def _make_S(self):
        for i in range(self.N):
            for j in range(i, self.N):
                temp = self.arr.pop(0)
                if temp == "+":
                    self.S[i][j] = 1
                elif temp == "-":
                    self.S[i][j] = -1

    def result(self):
        self.answer = [0 for _ in range(self.N)]
        self._make_S()
        self._backtracking(index=0)
        print(" ".join(map(str, self.answer)))

if __name__ == '__main__':
    # input = open('./1248.txt')
    P = P()
    P.result()