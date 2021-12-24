from sys import stdin as input

class P8320:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        count = 0
        for i in range(1, self.N + 1):
            for j in range(1, i + 1):
                if (i * j) <= self.N:
                    print(i, j)
                    count += 1
        print(count)


if __name__ == '__main__':
    input = open('./8320.txt')
    P = P8320()
    P.input_data()
    P.result()