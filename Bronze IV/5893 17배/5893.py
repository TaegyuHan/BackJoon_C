from sys import stdin as input

class P5893:

    def input_data(self):
        self.bin_num = int(input.readline(), 2)

    def result(self):
        multi = 17
        print(str(bin(self.bin_num * multi))[2:])

if __name__ == '__main__':
    # input = open('./5893.txt')
    P = P5893()
    P.input_data()
    P.result()