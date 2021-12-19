from sys import stdin as input


class P15873:

    def input_data(self):
        self.num = input.readline()

    def result(self):
        num_len = len(self.num)
        if num_len == 2:
            print(int(self.num[0]) + int(self.num[1]))
        elif self.num[1] == '0':
            print(int(self.num[:2]) + int(self.num[2:]))
        else:
            print(int(self.num[:1]) + int(self.num[1:]))


if __name__ == '__main__':
    # input = open('./15873.txt')
    P = P15873()
    P.input_data()
    P.result()