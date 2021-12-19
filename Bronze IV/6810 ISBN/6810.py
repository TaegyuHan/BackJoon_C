from sys import stdin as input

class P6810:

    def input_data(self):
        self.a = int(input.readline())
        self.b = int(input.readline())
        self.c = int(input.readline())

    def result(self):
        answer = "The 1-3-sum is "
        answer += str(91 + self.a * 1 + self.b * 3 + self.c * 1)
        print(answer)


if __name__ == '__main__':
    # input = open('./6810.txt')
    P = P6810()
    P.input_data()
    P.result()