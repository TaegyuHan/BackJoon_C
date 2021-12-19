from sys import stdin as input

class P21354:

    def input_data(self):
        self.apple_count, self.pear_count = map(int, input.readline().split())

    def result(self):
        Axel = self.apple_count * 7
        Petra = self.pear_count * 13
        if Axel > Petra:
            print("Axel")
        elif Axel < Petra:
            print("Petra")
        else:
            print("lika")


if __name__ == '__main__':
    # input = open('./21354.txt')
    P = P21354()
    P.input_data()
    P.result()