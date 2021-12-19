from sys import stdin as input

class P23825:

    def input_data(self):
        self.S, self.A = map(int, input.readline().split())

    def result(self):
        print(min(self.S//2, self.A//2))


if __name__ == '__main__':
    # input = open('./23825.txt')
    P = P23825()
    P.input_data()
    P.result()