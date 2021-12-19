from sys import stdin as input

class P15726:

    def input_data(self):
        self.A, self.B, self.C = map(int, input.readline().split())

    def result(self):
        print(int(max(self.A / self.B * self.C, self.A * self.B / self.C)))

if __name__ == '__main__':
    # input = open('./15726.txt')
    P = P15726()
    P.input_data()
    P.result()