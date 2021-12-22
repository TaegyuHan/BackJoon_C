from sys import stdin as input

class P9316:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        for i in range(1, self.N + 1):
            print(f"Hello World, Judge {i}!")

if __name__ == '__main__':
    # input = open('./9316.txt')
    P = P9316()
    P.input_data()
    P.result()