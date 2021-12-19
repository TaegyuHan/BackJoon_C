from sys import stdin as input

class P15700:

    def input_data(self):
        self.N, self.M = map(int, input.readline().split())

    def result(self):
        print(max(self.N *  self.M // 2, self.M *  self.N // 2))


if __name__ == '__main__':
    # input = open('./15700.txt')
    P = P15700()
    P.input_data()
    P.result()