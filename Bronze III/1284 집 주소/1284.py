from sys import stdin as input

class P1284:

    def input_data(self):
        while input_num := input.readline().rstrip():
            if input_num == "0": break
            self._result(input_num)

    def _number_gap(self, num):
        return len(str(num)) - 1

    def _number_side(self, num):
        return 2

    def _check_num(self, num):
        if num == "1":
            return 2
        elif num == "0":
            return 4
        else:
            return 3

    def _result(self, numbers):
        asnwer = 0
        asnwer += self._number_gap(numbers)
        asnwer += self._number_side(numbers)
        for num in numbers:
            asnwer += self._check_num(num)
        print(asnwer)


if __name__ == '__main__':
    # input = open('./1284.txt')
    P = P1284()
    P.input_data()