from sys import stdin as input
from dataclasses import dataclass

class P:

    def __change_board(self) -> None:
        self.board[0][0], self.board[0][1], \
        self.board[1][0], self.board[1][1] = \
            self.board[1][0], self.board[0][0], \
            self.board[1][1], self.board[0][1]

    def __calculation(self) -> int:
        sum = (self.board[0][0] / self.board[1][0]) + \
              (self.board[0][1] / self.board[1][1])
        return sum

    def __show(self) -> None:
        for row in self.board:
            print(" ".join(map(str, row)))
        print()

    def __input_data(self) -> None:
        self.board = [list(map(int, input.readline().split())) for _ in range(2)]

    def result(self) -> None:
        self.__input_data()
        calculation_list = []
        for i in range(1, 5):
            self.__change_board()
            calculation_list.append(self.__calculation())
            # self.__show()

        max_value = max(calculation_list)
        print((calculation_list.index(max_value) + 1) % 4)


if __name__ == '__main__':
    # input = open('./2863.txt')
    P = P()
    P.result()