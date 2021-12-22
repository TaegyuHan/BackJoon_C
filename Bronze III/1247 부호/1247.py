from sys import stdin as input

class P1247:

    def input_data(self):
        self.TEST_COUNT = 3

    def _symbol(self, num):
        if num > 0:
            return "+"
        elif num < 0:
            return "-"
        else:
            return "0"

    def result(self):
        for _ in range(self.TEST_COUNT):
            input_number_count = int(input.readline())
            tmp_sum = 0
            for _ in range(input_number_count):
                tmp_sum += int(input.readline())
            print(self._symbol(tmp_sum))


if __name__ == '__main__':
    # input = open('./1247.txt')
    P = P1247()
    P.input_data()
    P.result()