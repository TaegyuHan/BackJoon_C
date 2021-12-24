from sys import stdin as input

class P:

    def input_data(self):
        self.N = int(input.readline())
        self.nl = list(map(int, input.readline().split()))

    @staticmethod
    def gcd(a, b):
        if (a == 0):
            return b
        return P.gcd(b % a, a)

    def result(self):
        gcd_number = P.gcd(self.nl[0], P.gcd(self.nl[1], self.nl[-1]))
        for i in range(1, (gcd_number // 2) + 1):
            if gcd_number % i == 0:
                print(i)
        print(gcd_number)


if __name__ == '__main__':
    # input = open('./5618.txt')
    P = P()
    P.input_data()
    P.result()