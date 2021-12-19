from sys import stdin as input

class P18005:

    def input_data(self):
        self.n = int(input.readline())

    def result(self):
        if self.n%2 == 1:
            print(0)
        elif self.n//2%2 == 0:
            print(2)
        else:
            print(1)


if __name__ == '__main__':
    # input = open('./18005.txt')
    P = P18005()
    P.input_data()
    P.result()