from sys import stdin as input

class P1037:

    def input_data(self):
        self.N = int(input.readline())
        self.number_list_A = list(map(int, input.readline().split()))
        self.number_list_A_max = max(self.number_list_A)
        self.number_list_A_min = min(self.number_list_A)

    def result(self):
        print(self.number_list_A_max *  self.number_list_A_min)


if __name__ == '__main__':
    # input = open("./1037.txt")
    P = P1037()
    P.input_data()
    P.result()