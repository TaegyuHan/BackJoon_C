from sys import stdin as input
# from dataclasses import dataclass

class P:

    def input_data(self):
        self.N = map(int, input.readline().split())

    def result(self):
        print(sum(self.N))


if __name__ == '__main__':
    # input = open('./11023.txt')
    P = P()
    P.input_data()
    P.result()