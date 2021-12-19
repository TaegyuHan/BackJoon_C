from sys import stdin as input

class P13597:

    def input_data(self):
        self.D, self.H, self.M = map(int, input.readline().split())

    def result(self):
        t1 = self.D * 24 * 60 + self.H * 60  + self.M
        t2 = 11 * 24 * 60 + 11 * 60 + 11
        t = t1 - t2
        if t < 0:
            print(-1)
        else:
            print(t)

if __name__ == '__main__':
    # input = open('./5928.txt')
    P = P13597()
    P.input_data()
    P.result()