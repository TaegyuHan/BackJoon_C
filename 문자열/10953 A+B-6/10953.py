from sys import stdin as input

class P10953:
    def __init__(self):
        self.A = 0
        self.B = 0

    def input_data(self):
        self.A, self.B = map(int, input.readline().rstrip().split(","))

    def result(self):
        for _ in range(int(input.readline())):
            self.input_data()
            print(self.A + self.B)

if __name__ == "__main__":
    # input = open("./10953.txt")
    P = P10953()
    P.result()