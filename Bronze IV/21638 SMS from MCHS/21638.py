from sys import stdin as input

class P21638:

    def input_data(self):
        self.t1, self.v1 = map(int, input.readline().split())
        self.t2, self.v2 = map(int, input.readline().split())

    def result(self):
        if self.t2 < 0 and self.v2 >= 10:
            print("A storm warning for tomorrow! Be careful and stay home if possible!")
        elif self.t1 > self.t2:
            print("MCHS warns! Low temperature is expected tomorrow.")
        elif self.v1 < self.v2:
            print("MCHS warns! Strong wind is expected tomorrow.")
        else:
            print("No message")


if __name__ == '__main__':
    # input = open('./21638.txt')
    P = P21638()
    P.input_data()
    P.result()