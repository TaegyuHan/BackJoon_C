from sys import stdin as input

class P9295:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    def result(self):
        for i in range(1, self.TEST_CASE + 1):
            sum_num = sum(map(int, input.readline().split()))
            print(f"Case {i}: {sum_num}")


if __name__ == '__main__':
    # input = open('./9295.txt')
    P = P9295()
    P.input_data()
    P.result()