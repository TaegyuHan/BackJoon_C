from sys import stdin as input

class P6788:

    def input_data(self):
        self.antenna = int(input.readline())
        self.eyes = int(input.readline())

    def result(self):
        if self.antenna >= 3 and self.eyes <= 4:
            print("TroyMartian")

        if self.antenna <= 6 and self.eyes >= 2:
            print("VladSaturnian")

        if self.antenna <= 2 and self.eyes <= 3:
            print("GraemeMercurian")


if __name__ == '__main__':
    # input = open('./6788.txt')
    P = P6788()
    P.input_data()
    P.result()