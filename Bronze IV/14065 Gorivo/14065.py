from sys import stdin as input

class P14065:

    def input_data(self):
        self.x = float(input.readline())

    def result(self):
        answer = 100.0 / ((1.609344 / 3.785411784) * self.x)
        print("%.6f" % answer)


if __name__ == '__main__':
    # input = open('./14065.txt')
    P = P14065()
    P.input_data()
    P.result()