from sys import stdin as input

class P2903:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        k, point = 2, 3
        for i in range(1, self.N):
            point += k
            k *= 2
        print(point * point)


if __name__ == '__main__':
    # input = open('./2903.txt')
    P = P2903()
    P.input_data()
    P.result()