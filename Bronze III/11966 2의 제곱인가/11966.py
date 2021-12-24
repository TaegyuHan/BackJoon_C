from sys import stdin as input

class P11966:

    def input_data(self):
        self.N = int(input.readline())

    def _check(self, n):
        if 2 ** n == self.N:
            print(1)
        else:
            print(0)

    def result(self):
        n = 0
        while True:
            if self.N <= 2**n:
                self._check(n)
                break
            n += 1


if __name__ == '__main__':
    # input = open('./11966.txt')
    P = P11966()
    P.input_data()
    P.result()