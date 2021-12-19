from sys import stdin as input

class P18408:

    def input_data(self):
        self.num_list = list(map(int, input.readline().split()))

    def _check_count(self):
        check_two = 0
        check_one = 0
        for num in self.num_list:
            if num == 2:
                check_two += 1
            else:
                check_one += 1

        if check_one > check_two:
            return 1
        else:
            return 2

    def result(self):
        print(self._check_count())


if __name__ == '__main__':
    # input = open('./18408.txt')
    P = P18408()
    P.input_data()
    P.result()