from sys import stdin as input

class P10815:

    def input_data(self):
        self.N = int(input.readline())
        self.N_number_list = set(map(int, input.readline().split()))

        self.M = int(input.readline())
        self.M_number_list = list(map(int, input.readline().split()))

    def result(self):
        for num in self.M_number_list:
            if num in self.N_number_list:
                print(1, end=" ")
            else:
                print(0, end=" ")


if __name__ == '__main__':
    # input = open("./10815.txt")
    P = P10815()
    P.input_data()
    P.result()