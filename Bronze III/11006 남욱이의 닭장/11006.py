from sys import stdin as input

class P11006:

    def input_data(self):
        self.T = int(input.readline())

    def result(self):
        for _ in range(self.T):
            N, M = map(int , input.readline().split())
            print(M * 2 - N, M - (M * 2 - N))


if __name__ == '__main__':
    # input = open('./11006.txt')
    P = P11006()
    P.input_data()
    P.result()