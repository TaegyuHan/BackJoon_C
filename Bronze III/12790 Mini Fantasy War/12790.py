from sys import stdin as input

class P12790:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    def _check_HP_MP(self, point):
        if point < 1:
            return 1
        else:
            return point

    def _check_A(self, point):
        if point < 0:
            return 0
        else:
            return point

    def result(self):
        for _ in range(self.TEST_CASE):
            HP, MP, A, B, I_HP, I_MP, I_A, I_B = \
                map(int, input.readline().split())

            HP = self._check_HP_MP(HP + I_HP)
            MP = self._check_HP_MP(MP + I_MP)
            A = self._check_A(A + I_A)
            B = B + I_B

            print(1 * HP + 5 * MP + 2 * A + 2 * B)


if __name__ == '__main__':
    # input = open('./12790.txt')
    P = P12790()
    P.input_data()
    P.result()