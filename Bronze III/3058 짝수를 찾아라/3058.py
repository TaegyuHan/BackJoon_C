from sys import stdin as input

class P3058:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    def _find_even_number(self):
        sum_num = 0
        min_even_num = 100
        for num in map(int, input.readline().split()):
            if num % 2 == 0:
                sum_num += num
                if min_even_num > num:
                   min_even_num = num

        print(sum_num, min_even_num)

    def result(self):
        for _ in range(self.TEST_CASE):
            self._find_even_number()

if __name__ == '__main__':
    # input = open('./3058.txt')
    P = P3058()
    P.input_data()
    P.result()