from sys import stdin as input

class P1964:

    def input_data(self):
        self.N = int(input.readline())

    def _pentagon(self, num):
        point = (4 * num) + 1 + (((num - 1) * num / 2) * 3)
        return int(point) % 45678

    def result(self):
        print(self._pentagon(self.N))


if __name__ == '__main__':
    # input = open('./1964.txt')
    P = P1964()
    P.input_data()
    P.result()