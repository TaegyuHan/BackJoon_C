from sys import stdin as input

class P1011:

    def input_data(self):
        self.T = int(input.readline())
        for _ in range(self.T):
            self.x, self.y = map(int, input.readline().split())
            self.tmp = self.y - self.x
            self._result()

    def _result(self):
        i = 0
        while True:
            if self.tmp <= i * (i + 1):
                break
            i += 1

        if self.tmp <= i ** 2:
            print(i * 2 - 1)
        else:
            print(i * 2)

if __name__ == '__main__':
    # input = open("./1011.txt")
    P = P1011()
    P.input_data()
