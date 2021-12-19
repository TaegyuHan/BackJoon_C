from sys import stdin as input

class P23375:

    def input_data(self):
        self.x, self.y = map(int, input.readline().split())
        self.r = int(input.readline())

    def result(self):
        print(self.x + self.r, self.y + self.r)
        print(self.x + self.r, self.y - self.r)
        print(self.x - self.r, self.y - self.r)
        print(self.x - self.r, self.y + self.r)

if __name__ == '__main__':
    # input = open('./23375.txt')
    P = P23375()
    P.input_data()
    P.result()