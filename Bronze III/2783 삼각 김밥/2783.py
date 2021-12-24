from sys import stdin as input

class P2783:

    def input_data(self):
        self.seven = tuple(map(int, input.readline().split()))
        self.N = int(input.readline())
        self.convenience_stores = [tuple(map(int, input.readline().split())) for _  in range(self.N)]

    def result(self):
        MAX_GRAM = 1_000
        min_price = MAX_GRAM / self.seven[1] * self.seven[0]
        for price, gram in self.convenience_stores:
            if min_price > (tmp := MAX_GRAM / gram * price):
                min_price = tmp

        print(round(min_price, 2))

if __name__ == '__main__':
    # input = open('./2783.txt')
    P = P2783()
    P.input_data()
    P.result()