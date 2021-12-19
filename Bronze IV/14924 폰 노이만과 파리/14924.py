from sys import stdin as input

class P14924:

    def input_data(self):
        self.S, self.T, self.D = map(int, input.readline().split())

    def result(self):
        second = self.D / (self.S*2)
        print(int(self.T * second))


if __name__ == '__main__':
    # input = open('./14924.txt')
    P = P14924()
    P.input_data()
    P.result()