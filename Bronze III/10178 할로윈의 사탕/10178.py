from sys import stdin as input

class P10178:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    def _div_candy(self):
        candy, people = map(int, input.readline().split())
        div = candy // people
        rest = candy % people
        print(f"You get {div} piece(s) and your dad gets {rest} piece(s).")

    def result(self):
        for _ in range(self.TEST_CASE):
            self._div_candy()


if __name__ == '__main__':
    # input = open('./10178.txt')
    P = P10178()
    P.input_data()
    P.result()