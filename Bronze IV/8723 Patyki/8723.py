from sys import stdin as input

class P8723:

    def input_data(self):
        self.a, self.b, self.c = sorted(map(int, input.readline().split()))

    def result(self):
        if self.a == self.b and \
                self.b == self.c and \
                self.c == self.a:
            print(2)

        elif self.c*self.c == self.b*self.b + self.a*self.a:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    # input = open('./8723.txt')
    P = P8723()
    P.input_data()
    P.result()