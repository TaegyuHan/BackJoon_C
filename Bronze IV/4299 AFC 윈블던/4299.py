from sys import stdin as input

class P4299:

    def input_data(self):
        self.P, self.M = map(int, input.readline().split())

    def result(self):
        if (self.P - self.M < 0) or (self.P - self.M)%2 != 0:
            print(-1)
        else:
            p = (self.P - self.M) // 2
            q = (self.P - p)

            print(max(p, q), min(p, q))


if __name__ == '__main__':
    # input = open('./4299.txt')
    P = P4299()
    P.input_data()
    P.result()