from sys import stdin as input

class P13985:

    def input_data(self):
        self.quize = input.readline().split()

    def result(self):
        result = str(eval("".join(self.quize[:3])))
        if result == self.quize[-1]:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    # input = open('./13985.txt')
    P = P13985()
    P.input_data()
    P.result()