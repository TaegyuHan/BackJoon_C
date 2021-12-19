from sys import stdin as input

class P18330:

    def input_data(self):
        self.n = int(input.readline())
        self.k = int(input.readline()) + 60

    def result(self):
        if self.n <= self.k:
            print(self.n * 1_500)
        else:
            print(self.k * 1_500 + (self.n - self.k) * 3_000)

if __name__ == '__main__':
    # input = open('18330.txt')
    P = P18330()
    P.input_data()
    P.result()