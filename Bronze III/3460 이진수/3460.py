from sys import stdin as input

class P3460:

    def input_data(self):
        self.TEST_COUNT = int(input.readline())

    def _bin_one_count(self, num):
        index = []
        for i, n in enumerate(reversed(str(bin(num))[2:])):
            if n == "1":
                index.append(str(i))
        print(" ".join(index))

    def result(self):
        for _ in range(self.TEST_COUNT):
            self._bin_one_count(int(input.readline()))


if __name__ == '__main__':
    # input = open('./3460.txt')
    P = P3460()
    P.input_data()
    P.result()