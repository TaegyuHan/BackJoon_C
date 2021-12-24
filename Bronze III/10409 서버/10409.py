from sys import stdin as input
from dataclasses import dataclass

class P:

    def input_data(self):
        self.n, self.T = map(int, input.readline().split())
        self.tasks = list(map(int, input.readline().split()))

    def result(self):
        sum_time = 0
        answer = 0
        for task_time in self.tasks:
            sum_time += task_time
            if self.T < sum_time:
                break
            answer += 1

        print(answer)


if __name__ == '__main__':
    # input = open('./10409.txt')
    P = P()
    P.input_data()
    P.result()