from sys import stdin as input

class P4180:

    def _show_board(self):
        for row in self.borad:
            for col in row:
                print(col, end="")
            print()

    def _chcek_boom(self, h, w):
        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        y = [-1, 0, 1, -1, 1, -1, 0, 1]
        boom_count = 0

        for i in range(len(x)):
            check_x = h + x[i]
            check_y = w + y[i]
            if check_x < 0 or check_y < 0:
                continue
            if check_x >= self.H or check_y >= self.W:
                continue
            if self.borad[check_x][check_y] == "*":
                boom_count += 1

        self.borad[h][w] = boom_count

    def input_data(self):
        while True:
            self.H, self.W = map(int, input.readline().split())

            # 0 들어오면 멈춤
            if self.H == 0 and self.W == 0:
                break

            # 보드 만들기
            self.borad = [list(input.readline().rstrip()) for _ in range(self.H)]

            for h in range(self.H):
                for w in range(self.W):
                    if self.borad[h][w] == ".":
                        self._chcek_boom(h, w)

            self._show_board()


if __name__ == '__main__':
    # input = open("./4108.txt")
    P = P4180()
    P.input_data()