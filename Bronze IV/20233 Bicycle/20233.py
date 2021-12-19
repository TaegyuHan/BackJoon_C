from sys import stdin as input

class P20233:

    def input_data(self):
        self.a = int(input.readline())
        self.x = int(input.readline())
        self.b = int(input.readline())
        self.y = int(input.readline())
        self.T = int(input.readline())

    def result(self):
        A = self.a + max(self.T - 30, 0) * self.x * 21
        B = self.b + max(self.T - 45, 0) * self.y * 21
        print(A, B)

if __name__ == '__main__':
    # input = open('./20233.txt')
    P = P20233()
    P.input_data()
    P.result()