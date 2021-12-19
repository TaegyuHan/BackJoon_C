from sys import stdin as input

class P16199:

    def input_data(self):
        self.b_year, self.b_month, self.b_date = map(int, input.readline().split())
        self.c_year, self.c_month, self.c_date = map(int, input.readline().split())

    def result(self):
        if self.c_month > self.b_month:
            print(self.c_year - self.b_year)
        elif self.c_month == self.b_month:
            if self.c_date >= self.b_date:
                print(self.c_year - self.b_year)
            else:
                print(self.c_year - self.b_year - 1)
        else:
            print(self.c_year - self.b_year - 1)

        print(self.c_year - self.b_year + 1) # 한국 나이
        print(self.c_year - self.b_year) # 연 나이


if __name__ == '__main__':
    # input = open('./16199.txt')
    P = P16199()
    P.input_data()
    P.result()