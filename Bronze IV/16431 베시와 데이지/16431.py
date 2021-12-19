from sys import stdin as input

class P16431:

    def input_data(self):
        self.B_x, self.B_y = map(int, input.readline().split())
        self.D_x, self.D_y = map(int, input.readline().split())
        self.C_x, self.C_y = map(int, input.readline().split())

    def result(self):
        D_move = abs(self.D_x - self.C_x) + abs(self.D_y - self.C_y)
        B_move = max(abs(self.B_x - self.C_x), abs(self.B_y - self.C_y))

        if B_move > D_move:
            print("daisy")
        elif  B_move < D_move:
            print("bessie")
        else:
            print("tie")


if __name__ == '__main__':
    # input = open('./16431.txt')
    P = P16431()
    P.input_data()
    P.result()