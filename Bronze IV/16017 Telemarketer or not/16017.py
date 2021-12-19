from sys import stdin as input

class P16017:

    def input_data(self):
        self.num1 = int(input.readline())
        self.num2 = int(input.readline())
        self.num3 = int(input.readline())
        self.num4 = int(input.readline())

    def result(self):
        chec_num = [8, 9]
        if self.num1 in chec_num and \
            self.num4 in chec_num and \
                self.num2 == self.num3:
            print("ignore")
        else:
            print("answer")


if __name__ == '__main__':
    # input = open('./16017.txt')
    P = P16017()
    P.input_data()
    P.result()