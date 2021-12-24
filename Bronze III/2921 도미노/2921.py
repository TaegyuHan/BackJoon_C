from sys import stdin as input

class P2921:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        sum = 0
        for i in range(self.N + 1):
            for j in range(i, self.N + 1):
                sum += i + j
        print(sum)


if __name__ == '__main__':
    # input = open('./2921.txt')
    P = P2921()
    P.input_data()
    P.result()