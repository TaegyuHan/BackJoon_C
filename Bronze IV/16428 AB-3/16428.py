from sys import stdin as input

class P16428:

    def input_data(self):
        self.A, self.B = map(int, input.readline().split())

    def result(self):
        c, d = self.A // self.B, self.A % self.B
        if self.A != 0 and d < 0:
            c, d = c + 1, d - self.B

        print(c)
        print(d)

if __name__ == '__main__':
    # input = open('./16428.txt')
    P = P16428()
    P.input_data()
    P.result()