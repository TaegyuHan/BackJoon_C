from sys import stdin as input

class P8718:

    def input_data(self):
        self.x, self.k = map(int, input.readline().split())

    def result(self):
        if self.k * 7 <= self.x: print(self.k * 7000)
        elif self.k * 3.5 <= self.x: print(self.k * 3500)
        elif self.k * 1.75 <= self.x: print(self.k * 1750)
        else: print(0)


if __name__ == '__main__':
    # input = open('./8718.txt')
    P = P8718()
    P.input_data()
    P.result()