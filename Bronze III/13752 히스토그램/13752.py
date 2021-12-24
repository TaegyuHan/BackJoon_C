from sys import stdin as input

class P13752:

    def input_data(self):
        self.n = int(input.readline())

    def result(self):
        for _ in range(self.n):
            print("=" * int(input.readline()))


if __name__ == '__main__':
    # input = open('./13752.txt')
    P = P13752()
    P.input_data()
    P.result()