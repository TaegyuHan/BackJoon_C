from sys import stdin as input

class P15051:

    def input_data(self):
        self.A1 = int(input.readline())
        self.A2 = int(input.readline())
        self.A3 = int(input.readline())

    def result(self):
        r1 = self.A2 * 2 + self.A3 * 4
        r2 = self.A1 * 2 + self.A3 * 2
        r3 = self.A1 * 4 + self.A2 * 2
        print(min(min(r1, r2), r3))

if __name__ == '__main__':
    # input = open('./15051.txt')
    P = P15051()
    P.input_data()
    P.result()