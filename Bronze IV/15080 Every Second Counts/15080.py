from sys import stdin as input

class P15080:

    def input_data(self):
        self.hour1, self.minute1, self.second1 = map(int, input.readline().rstrip().split(":"))
        self.hour2, self.minute2, self.second2 = map(int, input.readline().rstrip().split(":"))

    def result(self):
        tmp_minte = 3_600
        second1_sum = self.hour1 * tmp_minte + self.minute1 * 60 + self.second1
        second2_sum = self.hour2 * tmp_minte + self.minute2 * 60 + self.second2

        if second1_sum > second2_sum:
            print(((24 * tmp_minte) + second2_sum) - second1_sum)
        else:
            print(second2_sum - second1_sum)


if __name__ == '__main__':
    # input = open('./15080.txt')
    P = P15080()
    P.input_data()
    P.result()