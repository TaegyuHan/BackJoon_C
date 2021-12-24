from sys import stdin as input
from dataclasses import dataclass

class P:

    def input_data(self):
        self.N = int(input.readline())
        self.people = list(map(int, input.readline().split()))

    def result(self):
        answer = 0
        for man1, man2, in zip(sorted(self.people), self.people):
            if man1 != man2:
                answer += 1
        print(answer)


if __name__ == '__main__':
    # input = open('./14656.txt')
    P = P()
    P.input_data()
    P.result()