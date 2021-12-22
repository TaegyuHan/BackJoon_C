from sys import stdin as input

class P2511:

    def input_data(self):
        self.A_cards = map(int, input.readline().split())
        self.B_cards = map(int, input.readline().split())
        self.A_win = 0
        self.B_win = 0
        self.last_win = ''

    def _check_win(self, i, a, b):
        if a > b:
            self.A_win += 3
            self.last_win = 'A'
        elif a < b:
            self.B_win += 3
            self.last_win = 'B'
        else:
            self.A_win += 1
            self.B_win += 1

    def _show_point(self, winner):
        print(self.A_win, self.B_win)
        print(winner)

    def _show_win(self):
        if self.A_win > self.B_win:
            self._show_point("A")
        elif self.A_win < self.B_win:
            self._show_point("B")
        else: # 점수가 같은 경우
            if self.last_win == "A":
                self._show_point("A")
            elif self.last_win == "B":
                self._show_point("B")
            else:
                self._show_point("D")

    def result(self):
        for i, (a, b) in enumerate(zip(self.A_cards, self.B_cards)):
            self._check_win(i, a, b)
        self._show_win()


if __name__ == '__main__':
    # input = open('./2511.txt')
    P = P2511()
    P.input_data()
    P.result()