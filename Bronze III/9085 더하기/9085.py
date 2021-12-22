from sys import stdin as input


class P9085:

    def input_data(self):
        self.TEST_COUNT = int(input.readline())

    def result(self):
        for _ in range(self.TEST_COUNT):
            self.NUM_COUNT = int(input.readline())
            print(sum(map(int, input.readline().split())))


if __name__ == '__main__':
    # input = open('./9085.txt')
    P = P9085()
    P.input_data()
    P.result()