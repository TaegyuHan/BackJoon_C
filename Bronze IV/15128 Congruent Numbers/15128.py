from sys import stdin as input

class P15128:

    def input_data(self):
        self.p1, self.q1, self.p2, self.q2 = map(int, input.readline().split())

    def result(self):
        if self.p1 * self.p2 % (self.q1 * self.q2 * 2) == 0:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    # input = open('./15128.txt')
    P = P15128()
    P.input_data()
    P.result()