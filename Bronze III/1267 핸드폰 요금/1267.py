from sys import stdin as input


class P1267:

    def input_data(self):
        self.CALL_COUNT = int(input.readline())

    def _Y_fee(self, time):
        fee_count = time // 30
        if fee_count == 0:
            return 10
        else:
            return fee_count * 10 + 10

    def _M_fee(self, time):
        fee_count = time // 60
        if fee_count == 0:
            return 15
        else:
            return fee_count * 15 + 15

    def result(self):
        M_fee_sum = 0
        Y_fee_sum = 0
        for time in map(int, input.readline().split()):
            M_fee_sum += self._M_fee(time)
            Y_fee_sum += self._Y_fee(time)

        if M_fee_sum == Y_fee_sum:
            print("Y", "M", M_fee_sum)
        elif M_fee_sum < Y_fee_sum:
            print("M", M_fee_sum)
        else:
            print("Y", Y_fee_sum)


if __name__ == '__main__':
    # input = open('./1267.txt')
    P = P1267()
    P.input_data()
    P.result()