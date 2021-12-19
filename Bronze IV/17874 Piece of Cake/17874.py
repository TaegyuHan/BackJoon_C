from sys import stdin as input

class P17874:

    def input_data(self):
        self.n, self.h, self.v = map(int, input.readline().split())

    def result(self):
        print(4 * max(self.n - self.v, self.v) * max(self.n - self.h, self.h))


if __name__ == '__main__':
    # input = open('./17874.txt')
    P = P17874()
    P.input_data()
    P.result()