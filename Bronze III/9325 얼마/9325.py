from sys import stdin as input

class P9325:

    def input_data(self):
        self.TEST_COUNT = int(input.readline())

    def result(self):
        for _ in range(self.TEST_COUNT):
            total_price = 0
            total_price += int(input.readline())
            option_count = int(input.readline())
            for _ in range(option_count):
                count, price = map(int, input.readline().split())
                total_price += count * price
            print(total_price)


if __name__ == '__main__':
    # input = open('./9325.txt')
    P = P9325()
    P.input_data()
    P.result()