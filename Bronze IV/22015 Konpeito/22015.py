from sys import stdin as input

class P22015:

    def input_data(self):
        self.candy_list = list(map(int, input.readline().split()))
        self.max_count = max(self.candy_list)

    def result(self):
        answer = 0
        for candy in self.candy_list:
            if (tmp := self.max_count - candy) > 0:
                answer += tmp
        print(answer)


if __name__ == '__main__':
    # input = open('./22015.txt')
    P = P22015()
    P.input_data()
    P.result()