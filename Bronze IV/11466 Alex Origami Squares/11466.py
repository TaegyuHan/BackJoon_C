from sys import stdin as input

class P114666:

    def input_data(self):
        self.H, self.W = map(int, input.readline().split())

    def _chage_W_H(self):
        if self.H < self.W:
            tmp = self.H
            self.H = self.W
            self.W = tmp

    def result(self):
        self._chage_W_H()

        if self.H > self.W * 3:
            print("%.1f" %self.W)
        elif self.H > self.W * 1.5:
            print("%f" % (self.H / 3))
        else:
            print("%f" % (self.W / 2))


if __name__ == '__main__':
    # input = open('./11466.txt')
    P = P114666()
    P.input_data()
    P.result()