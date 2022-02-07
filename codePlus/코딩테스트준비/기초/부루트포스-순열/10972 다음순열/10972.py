"""Solution code for "BaekJoon 다음 순열".

- Problem link: https://www.acmicpc.net/problem/10972
"""

from sys import stdin as input

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.numbers = list(map(int, input.readline().split()))
        self.index = 0

    def result(self) -> None:
        for i in range(self.N - 1, 0, -1):
            if self.numbers[i - 1] < self.numbers[i]:
                for j in range(self.N - 1, 0, -1):
                    if self.numbers[i - 1] < self.numbers[j]:
                        self.numbers[i - 1], self.numbers[j] = self.numbers[j], self.numbers[i - 1]
                        self.answer = self.numbers[:i] + sorted(self.numbers[i:])
                        print(*self.answer)
                        return
        print(-1)


if __name__ == '__main__':
    # input = open('./10972.txt')
    P = P()
    P.result()