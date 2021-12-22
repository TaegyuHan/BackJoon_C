from sys import stdin as input

class P10569:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    def result(self):
        for _ in range(self.TEST_CASE):
            V, E = map(int, input.readline().split())
            print(E - V + 2)


if __name__ == '__main__':
    # input = open('./10569.txt')
    P = P10569()
    P.input_data()
    P.result()