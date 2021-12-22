from sys import stdin as input

class P10539:

    def input_data(self):
        self.NUMBER_COUNT = int(input.readline())
        self.number_list = map(int, input.readline().split())

    def result(self):
        sum = 0
        for i, num in enumerate(self.number_list):
            origin = (i + 1) * num - sum
            sum += origin
            print(origin)


if __name__ == '__main__':
    # input = open('./10539.txt')
    P = P10539()
    P.input_data()
    P.result()