from sys import stdin as input

class P20499:

    def input_data(self):
        self.K, self.D, self.A = map(int, input.readline().split("/"))

    def result(self):
        if self.K + self.A < self.D or self.D == 0:
            print("hasu")
        else:
            print("gosu")


if __name__ == '__main__':
    # input = open('./20499.txt')
    P = P20499()
    P.input_data()
    P.result()