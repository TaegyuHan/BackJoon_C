"""
    Solution code for "BaekJoon LSC2".

    - Problem link: https://www.acmicpc.net/problem/9252
"""

from sys import stdin as input


class D:
    STRING1 = "0"
    STRING1_LEN: int
    STRING2 = "0"
    STRING2_LEN: int
    BOARD = []
    ANSWER_STRING = ""
    ANSWER_COUNT = 0


class P:

    def __init__(self) -> None:
        D.STRING1 += input.readline().strip()
        D.STRING1_LEN = len(D.STRING1)
        D.STRING2 += input.readline().strip()
        D.STRING2_LEN = len(D.STRING2)
        self._init_board()

    def _show_board(self):
        """ 보드 확인하기 """
        print(*D.STRING1)
        for row in D.BOARD:
            print(*row)

    def _init_board(self):
        """ 보드 생성 """
        D.BOARD = [[0 for _ in range(D.STRING1_LEN)]
                   for _ in range(D.STRING2_LEN)]

        for row in range(1, D.STRING2_LEN):
            for col in range(1, D.STRING1_LEN):
                # 두 값이 같은 경우
                if D.STRING2[row] == D.STRING1[col]:
                    D.BOARD[row][col] = D.BOARD[row - 1][col - 1] + 1
                else:
                    D.BOARD[row][col] = max(
                        D.BOARD[row - 1][col],
                        D.BOARD[row][col - 1]
                    )

    def _find_string(self):
        """ 최장 공통 부분 수열 찾기 """
        row, col = D.STRING2_LEN - 1, D.STRING1_LEN - 1

        while D.BOARD[row][col]:
            # 왼쪽 값이 같은경우
            if D.BOARD[row][col] == D.BOARD[row][col - 1]:
                col -= 1
                continue
            elif D.BOARD[row][col] == D.BOARD[row - 1][col]:
                row -= 1
                continue

            D.ANSWER_STRING += D.STRING2[row]
            D.ANSWER_COUNT += 1
            row, col = row - 1, col - 1


    def run(self) -> None:
        # self._show_board()
        self._find_string()
        print(D.ANSWER_COUNT)
        print(D.ANSWER_STRING[::-1])

if __name__ == '__main__':
    # input = open('./9252.txt')
    P = P()
    P.run()