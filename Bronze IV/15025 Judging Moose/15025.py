from sys import stdin as input

class P15025:

    def input_data(self):
        self.L, self.R = map(int, input.readline().split())

    def result(self):
        if self.L == 0 and self.R == 0:
            print("Not a moose")
        elif self.L == self.R:
            print("Even", self.L*2)
        else:
            print("Odd", max(self.L, self.R)*2)


if __name__ == '__main__':
    # input = open('./15025.txt')
    P = P15025()
    P.input_data()
    P.result()