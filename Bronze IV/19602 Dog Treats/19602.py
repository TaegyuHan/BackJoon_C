from sys import stdin as input

class P19602:

    def input_data(self):
        self.S = int(input.readline())
        self.M = int(input.readline())
        self.L = int(input.readline())

    def result(self):
        score = 1*self.S + 2*self.M + 3*self.L
        if score >= 10:
            print("happy")
        else:
            print("sad")

if __name__ == '__main__':
    # input = open('./19602.txt')
    P = P19602()
    P.input_data()
    P.result()