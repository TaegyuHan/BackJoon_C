from sys import stdin as input

class P17903:

    def input_data(self):
        self.m, self.n = map(int, input.readline().split())

    def result(self):
        if self.m >= 8:
            print("satisfactory")
        else:
            print("unsatisfactory")

if __name__ == '__main__':
    # input = open('./17903.txt')
    P = P17903()
    P.input_data()
    P.result()