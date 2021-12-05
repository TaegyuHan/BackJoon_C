from sys import stdin as input

class P2743:
    def input_data(self):
        self.string = input.readline().rstrip()

    def result(self):
        print(len(self.string))

if __name__ == '__main__':
    # input = open("./2743.txt")
    P = P2743()
    P.input_data()
    P.result()
