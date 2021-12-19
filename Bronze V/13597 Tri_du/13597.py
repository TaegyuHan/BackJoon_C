from sys import stdin as input

class P13597:

    def input_data(self):
        self.A, self.B = map(int, input.readline().split())

    def result(self):
        if self.A >= self.B:
            print(self.A)
        else:
            print(self.B)

if __name__ == '__main__':
    # input = open("./13597.txt")
    P = P13597()
    P.input_data()
    P.result()
