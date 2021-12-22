from sys import stdin as input

class P2935:

    def input_data(self):
        self.num1 = input.readline().rstrip()
        self.symbol = input.readline().rstrip()
        self.num2 = input.readline().rstrip()

    def result(self):
        print(eval(self.num1 + self.symbol + self.num2))

if __name__ == '__main__':
    # input = open('./2935.txt')
    P = P2935()
    P.input_data()
    P.result()