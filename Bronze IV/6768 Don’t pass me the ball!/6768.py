from sys import stdin as input

class P6768:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        print((self.N - 1) * (self.N - 2) * (self.N - 3) // (3 * 2 * 1))


if __name__ == '__main__':
    # input = open('./6768.txt')
    P = P6768()
    P.input_data()
    P.result()