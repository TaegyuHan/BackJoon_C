from sys import stdin as input

class P13580:

    def input_data(self):
        self.num_list = sorted(map(int, input.readline().split()))

    def result(self):
        num = self.num_list
        if num[0] == num[1] or \
                num[1] == num[2] or \
                num[0] + num[1] == num[2]:
            print("S")
        else:
            print("N")

if __name__ == '__main__':
    # input = open('./13580.txt')
    P = P13580()
    P.input_data()
    P.result()