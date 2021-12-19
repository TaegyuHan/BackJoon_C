from sys import stdin as input

class P16727:

    def input_data(self):
        self.p1, self.s1 = map(int, input.readline().split())
        self.s2, self.p2 = map(int, input.readline().split())

    def result(self):
        p = self.p1 + self.p2
        s = self.s1 + self.s2

        if p == s:
            if self.p1 == self.s2:
                print("Penalty")
            elif self.p1 > self.s2:
                print("Esteghlal")
            else:
                print("Persepolis")
        elif p > s:
            print("Persepolis")
        else:
            print("Esteghlal")


if __name__ == '__main__':
    # input = open('./16727.txt')
    P = P16727()
    P.input_data()
    P.result()