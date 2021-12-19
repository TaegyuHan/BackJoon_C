from sys import stdin as input

class P14264:

    def input_data(self):
        self.L = int(input.readline())

    def result(self):
        print(3 ** 0.5 / 4 * self.L ** 2)

if __name__ == '__main__':
    # input = open('./14264.txt')
    P = P14264()
    P.input_data()
    P.result()