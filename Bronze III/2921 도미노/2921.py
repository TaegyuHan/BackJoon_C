from sys import stdin as input

class P2921:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        self.N * self.N * 3


if __name__ == '__main__':
    input = open('./2921.txt')
    P = P2921()
    P.input_data()
    P.result()