from sys import stdin as input

class P11282:

    def input_data(self):
        self.num = int(input.readline())

    def result(self):
        print(chr(self.num + 44031))


if __name__ == '__main__':
    # input = open('./11282.txt')
    P = P11282()
    P.input_data()
    P.result()