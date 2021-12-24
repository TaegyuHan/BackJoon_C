from sys import stdin as input

class P5361:

    def input_data(self):
        self.N = int(input.readline())
        self.item_price = [
            350.34,
            230.90,
            190.55,
            125.30,
            180.90
        ]

    def _sum_price(self, item_list):
        sum = 0
        for i, count in enumerate(item_list):
            sum += (self.item_price[i] * count)
        return sum

    def result(self):
        for _ in range(self.N):
            sum_price = self._sum_price(map(int, input.readline().split()))
            print(f"${round(sum_price, 2):.2f}")


if __name__ == '__main__':
    # input = open('./5361.txt')
    P = P5361()
    P.input_data()
    P.result()