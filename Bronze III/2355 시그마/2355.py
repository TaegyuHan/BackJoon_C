from sys import stdin as input

class P13597:

    def input_data(self):
        self.A, self.B = map(int, input.readline().split())
        self._compare()

    def _compare(self):
        if self.A > self.B:
            self.A, self.B = self.B, self.A

    def _sum_pp(self, a, b):
        print(((b * (b + 1)) // 2) - ((a * (a + 1)) // 2))

    def _sum_mp(self, a, b):
        a = -a
        print(((b * (b + 1)) // 2) - (((a * (a + 1)) // 2)))

    def _sum_mm(self, a, b):
        a, b = -a, -b
        print(-(((a * (a + 1)) // 2) - ((b * (b + 1)) // 2)))

    def result(self):
        if self.A > 0 and self.B > 0:
            self._sum_pp(self.A - 1, self.B)
        elif self.A < 0 and self.B > 0:
            self._sum_mp(self.A, self.B)
        else:
            self._sum_mm(self.A, self.B + 1)


if __name__ == '__main__':
    # input = open('./2355.txt')
    P = P13597()
    P.input_data()
    P.result()