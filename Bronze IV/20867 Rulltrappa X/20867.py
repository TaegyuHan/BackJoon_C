from sys import stdin as input

class P20867:

    def input_data(self):
        self.M, self.S, self.G = map(int, input.readline().rstrip().split(" "))
        self.A, self.B = map(int, input.readline().rstrip().split(" "))
        self.L, self.R = map(int, input.readline().rstrip().split(" "))

    def result(self):
        lwait = self.L / self.A
        rwait = self.R / self.B

        if self.M & self.G:
            ls = self.M / self.G + 1
        else:
            ls = self.M / self.G

        if self.M & self.S:
            rs = self.M / self.S + 1
        else:
            rs = self.M / self.S

        if ls < rs:
            if ls + lwait < rs + rwait:
                print("friskus")
            else:
                print("latmask")
        else:
            if ls + lwait < rs + rwait:
                print("friskus")
            else:
                print("latmask")

if __name__ == '__main__':
    input = open('./20867.txt')
    P = P20867()
    P.input_data()
    P.result()