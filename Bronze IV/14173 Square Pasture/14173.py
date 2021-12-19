from sys import stdin as input

class P14173:

    def input_data(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input.readline().split())
        self.x3, self.y3, self.x4, self.y4 = map(int, input.readline().split())

    def result(self):
        X = max(self.x2, self.x4) - min(self.x1, self.x3)
        Y = max(self.y2, self.y4) - min(self.y1, self.y3)
        print(max(X, Y) ** 2)

if __name__ == '__main__':
    # input = open('./14173.txt')
    P = P14173()
    P.input_data()
    P.result()

