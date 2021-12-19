from sys import stdin as input

class P216431:

    def input_data(self):
        self.a, self.b = map(int, input.readline().split())

    def result(self):
        if self.a >= self.b:
            print(self.b)
        else:
            print(self.a + 1)


if __name__ == '__main__':
    # input = open('./21631.txt')
    P = P216431()
    P.input_data()
    P.result()