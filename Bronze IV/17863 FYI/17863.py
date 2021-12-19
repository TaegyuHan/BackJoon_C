from sys import stdin as input

class P17863:

    def input_data(self):
        self.number = input.readline()

    def result(self):
        if self.number[:3] == "555":
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    # input = open('./17863.txt')
    P = P17863()
    P.input_data()
    P.result()