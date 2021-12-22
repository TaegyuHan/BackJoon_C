from sys import stdin as input

class P2959:

    def input_data(self):
        self.move = sorted(map(int, input.readline().split()))

    def result(self):
        print(self.move[0] * self.move[2])


if __name__ == '__main__':
    # input = open('./2959.txt')
    P = P2959()
    P.input_data()
    P.result()