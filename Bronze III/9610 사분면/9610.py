from sys import stdin as input

class P9610:

    def input_data(self):
        self.INPUT_POINT = int(input.readline())
        self.Q_list = [0, 0, 0, 0, 0]

    def _check_q(self, x, y):
        if x == 0 or y == 0:
            self.Q_list[0] += 1
        elif x > 0 and y > 0:
            self.Q_list[1] += 1
        elif x < 0 and y >  0:
            self.Q_list[2] += 1
        elif x < 0 and y < 0:
            self.Q_list[3] += 1
        elif x > 0 and y < 0:
            self.Q_list[4] += 1

    def result(self):
        for _ in range(self.INPUT_POINT):
            x, y = map(int, input.readline().split())
            self._check_q(x, y)

        for i in range(1, 5):
            print(f"Q{i}: {self.Q_list[i]}")
        print(f"AXIS: {self.Q_list[0]}")


if __name__ == '__main__':
    # input = open('./9610.txt')
    P = P9610()
    P.input_data()
    P.result()