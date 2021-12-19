from sys import stdin as input

class P6764:

    def input_data(self):
        self.A = int(input.readline())
        self.B = int(input.readline())
        self.C = int(input.readline())
        self.D = int(input.readline())

    def result(self):
        if self.A < self.B and self.B < self.C and self.C < self.D:
            print("Fish Rising")
        elif self.A > self.B and self.B > self.C and self.C > self.D:
            print("Fish Diving")
        elif self.A == self.B and self.B == self.C and self.C == self.D:
            print("Fish At Constant Depth")
        else:
            print("No Fish")


if __name__ == '__main__':
    # input = open('./6764.txt')
    P = P6764()
    P.input_data()
    P.result()