"""Solution code for "BaekJoon 체스".

- Problem link: https://www.acmicpc.net/problem/1986
"""

from sys import stdin as input
from dataclasses import dataclass


class Chess:
    QUEEN = "Q"
    KNIGHT = "K"
    PQWN = "P"
    CHESS_LIST = [QUEEN, KNIGHT, PQWN]


@dataclass
class Position:
    """ 체스말 위치 """
    row: int
    col: int


@dataclass
class Queen(Position):
    """ 퀸 """
    type = "Q"

    def __repr__(self):
        return "Q"


@dataclass
class Knight(Position):
    """ 나이트 """
    type = "K"

    def __repr__(self):
        return "K"


class KnightMove:
    """ 나이트 이동 하기 """
    LEFT_UP_1 = (-2, -1)
    LEFT_UP_2 = (-1, -2)

    LEFT_DOWN_1 = (1, -2)
    LEFT_DOWN_2 = (2, -1)

    RIGHT_UP_1 = (-2, 1)
    RIGHT_UP_2 = (-1, 2)

    RIGHT_DOWN_1 = (1, 2)
    RIGHT_DOWN_2 = (2, 1)

    ALL = [
        LEFT_UP_1,
        LEFT_UP_2,
        LEFT_DOWN_1,
        LEFT_DOWN_2,
        RIGHT_UP_1,
        RIGHT_UP_2,
        RIGHT_DOWN_1,
        RIGHT_DOWN_2
    ]


@dataclass
class Pawn(Position):
    """ 폰 """
    type = "P"

    def __repr__(self):
        return "P"


class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.board = [[0 for _ in range(self.M)] for _ in range(self.N)]
        self.board_check = [[True for _ in range(self.M)] for _ in range(self.N)]
        self.check_list = []
        self.anwer = self.N*self.M

    def _show_board(self):
        """ 체스판 확인 """
        for row in self.board:
            print(" ".join(map(str, row)))
        print()

    def _show_board_check(self):
        """ 확인 체스판 확인 """
        for row in self.board_check:
            print(" ".join(map(str, map(int, row))))
        print()

    def _check_knight(self, piece: Knight) -> None:
        """ 나이트 확인 """
        for trow, tcol in KnightMove.ALL:
            nrow, ncol = piece.row + trow, piece.col + tcol

            # 범위 확인
            if not (0 <= nrow < self.N and 0 <= ncol < self.M):
                continue

            # 말이있거나 확인 한곳
            if not self.board_check[nrow][ncol]:
                continue

            self.anwer -= 1
            self.board_check[nrow][ncol] = False

    def _check_queen(self, piece: Knight) -> None:
        """ 퀸 확인 """

        # 가로 세로
        LEFT = True
        RIGHT = True
        UP = True
        DOWN = True

        # 대각선
        LEFT_UP = True
        LEFT_DONW = True
        RIGHT_UP = True
        RIGHT_DOWN = True

        go = max(self.N, self.M)
        for i in range(1, go + 1):

            # 왼쪽
            if LEFT:
                # 범위 확인
                ncol = piece.col - i
                if not (0 <= ncol < self.M):
                    LEFT = False

                if LEFT and self.board[piece.row][ncol] != 0:
                    LEFT = False

                if LEFT:
                    if self.board_check[piece.row][ncol]:
                        self.board_check[piece.row][ncol] = False
                        self.anwer -= 1

            # 오른쪽
            if RIGHT:
                # 범위 확인
                ncol = piece.col + i
                if not (0 <= ncol < self.M):
                    RIGHT = False

                if RIGHT and self.board[piece.row][ncol] != 0:
                    RIGHT = False

                if RIGHT:
                    if self.board_check[piece.row][ncol]:
                        self.board_check[piece.row][ncol] = False
                        self.anwer -= 1

            # 위
            if UP:
                # 범위 확인
                nrow = piece.row - i
                if not (0 <= nrow < self.N):
                    UP = False

                if UP and self.board[nrow][piece.col] != 0:
                    UP = False

                if UP:
                    if self.board_check[nrow][piece.col]:
                        self.board_check[nrow][piece.col] = False
                        self.anwer -= 1

            # 아래
            if DOWN:
                # 범위 확인
                nrow = piece.row + i
                if not (0 <= nrow < self.N):
                    DOWN = False

                if DOWN and self.board[nrow][piece.col] != 0:
                    DOWN = False

                if DOWN:
                    if self.board_check[nrow][piece.col]:
                        self.board_check[nrow][piece.col] = False
                        self.anwer -= 1

            # 대각선 왼쪽 위
            if LEFT_UP:
                # 범위 확인
                nrow, ncol = piece.row - i, piece.col - i
                if not (0 <= nrow < self.N and 0 <= ncol < self.M):
                    LEFT_UP = False

                if LEFT_UP and self.board[nrow][ncol] != 0:
                    LEFT_UP = False

                if LEFT_UP:
                    if self.board_check[nrow][ncol]:
                        self.board_check[nrow][ncol] = False
                        self.anwer -= 1

            # 대각선 왼쪽 아래
            if LEFT_DONW:
                # 범위 확인
                nrow, ncol = piece.row + i, piece.col - i
                if not (0 <= nrow < self.N and 0 <= ncol < self.M):
                    LEFT_DONW = False

                if LEFT_DONW and self.board[nrow][ncol] != 0:
                    LEFT_DONW = False

                if LEFT_DONW:
                    if self.board_check[nrow][ncol]:
                        self.board_check[nrow][ncol] = False
                        self.anwer -= 1

            # 대각선 오른쪽 위
            if RIGHT_UP:
                # 범위 확인
                nrow, ncol = piece.row - i, piece.col + i
                if not (0 <= nrow < self.N and 0 <= ncol < self.M):
                    RIGHT_UP = False

                if RIGHT_UP and self.board[nrow][ncol] != 0:
                    RIGHT_UP = False

                if RIGHT_UP:
                    if self.board_check[nrow][ncol]:
                        self.board_check[nrow][ncol] = False
                        self.anwer -= 1

            # 대각선 오른쪽 아래
            if RIGHT_DOWN:
                # 범위 확인
                nrow, ncol = piece.row + i, piece.col + i
                if not (0 <= nrow < self.N and 0 <= ncol < self.M):
                    RIGHT_DOWN = False

                if RIGHT_DOWN and self.board[nrow][ncol] != 0:
                    RIGHT_DOWN = False

                if RIGHT_DOWN:
                    if self.board_check[nrow][ncol]:
                        self.board_check[nrow][ncol] = False
                        self.anwer -= 1

            if not (LEFT or RIGHT or UP or DOWN or LEFT_UP or LEFT_DONW or RIGHT_DOWN or RIGHT_UP):
                break

    def _safe_check(self):
        """ 안전한 칸 확인 """
        for piece in self.check_list:
            if piece.type == Chess.KNIGHT:
                self._check_knight(piece)
            elif piece.type == Chess.QUEEN:
                self._check_queen(piece)

    def _input_piece(self):
        """ 체스 데이터 받기 """
        for piece in Chess.CHESS_LIST:
            count, *position = map(int, input.readline().split())
            for i in range(count):
                row, col = map(lambda x: x - 1, position[i*2: i*2 + 2])

                if piece == Chess.QUEEN:
                    self.board[row][col] = Queen(row, col)
                elif piece == Chess.PQWN:
                    self.board[row][col] = Pawn(row, col)
                elif piece == Chess.KNIGHT:
                    self.board[row][col] = Knight(row, col)

                self.anwer -= 1
                self.board_check[row][col] = False
                self.check_list.append(self.board[row][col])


    def run(self) -> None:
        """ 실행 """
        self._input_piece()
        self._safe_check()
        # self._show_board()
        # self._show_board_check()
        print(self.anwer)

if __name__ == '__main__':
    # input = open('./1986.txt')
    P = P()
    P.run()
