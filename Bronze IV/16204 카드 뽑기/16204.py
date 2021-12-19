from sys import stdin as input

class P16204:

    def input_data(self):
        self.N, self.M, self.K = map(int, input.readline().split())

    def result(self):
        front_x = self.N - self.M
        back_x = self.N - self.K

        O = min(self.M, self.K)
        X = min(front_x, back_x)

        if O == X:
            print(O + X)
        else:
            print(min(self.M, self.K) + min(front_x, back_x))


if __name__ == '__main__':
    # input = open('./16204.txt')
    P = P16204()
    P.input_data()
    P.result()