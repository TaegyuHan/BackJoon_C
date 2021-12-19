from sys import stdin as input

class P14623:

    def input_data(self):
        self.bin1 = int(input.readline(), 2)
        self.bin2 = int(input.readline(), 2)

    def result(self):
        print(str(bin(self.bin1 * self.bin2))[2:])


if __name__ == '__main__':
    # input = open('./14623.txt')
    P = P14623()
    P.input_data()
    P.result()