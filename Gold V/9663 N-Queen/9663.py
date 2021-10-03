import sys

class BJ9663():

    def __init__(self) -> None:
        sys.stdin = open("./9663.txt")
        self.N = int(sys.stdin.readline())
        self.board = []
        self.check_col = []
        self.check_row = set()
        self.check_stack = []
        self.used_unit = 1

    def row_check(self, num) -> None:
        self.check_row.add(num)

    def col_check(self, col_index, num) -> None:
        back_num = num
        front_num = num
        for i in range(col_index - 1, -1, -1):
            back_num -= 1
            if back_num < 0:
                break
            self.check_col[i].add(back_num)

        for i in range(col_index + 1, self.N):
            front_num += 1
            if front_num >= self.N:
                break
            self.check_col[i].add(front_num)

    def board_init(self, i) -> None:
        self.board = [i] + [-1 for _ in range(self.N - 1)]
        self.check_col = [set() for _ in range(self.N)]
        self.col_check(0, i)
        self.check_row = {i}
        self.row_check(i)
        self.check_stack = [i]
        self.used_unit = 1

    def solved(self) -> int:
        for i in range(self.N):
            self.board_init(i)
            print(self.check_col)
            print(self.check_row)


a = BJ9663()
a.solved()
