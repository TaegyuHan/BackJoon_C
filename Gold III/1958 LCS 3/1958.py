"""
    Solution code for "BaekJoon LCS 3".

    - Problem link: https://www.acmicpc.net/problem/1958
"""

from sys import stdin as input


class D:
    """ 데이터 """
    STRING1 = "0"
    STRING2 = "0"
    STRING3 = "0"
    BOARD = []


class P:

    def __init__(self) -> None:
        D.STRING1 += input.readline().strip()
        D.STRING2 += input.readline().strip()
        D.STRING3 += input.readline().strip()

    def _show_board(self, board):
        """ 보드 확인하기 """
        for row in board:
            print(*row)

    def _lcs(self, string1, string2):
        """ 보드 생성 """
        string1_len, string2_len = len(string1), len(string2)
        board = [[0 for _ in range(string1_len)] for _ in range(string2_len)]
        lcs_string = ""

        # LSC 첫번째 구하기
        for row in range(1, string2_len):
            for col in range(1, string1_len):
                if string2[row] == string1[col]:
                   board[row][col] = board[row - 1][col - 1] + 1
                   lcs_string += string2[row]

        return lcs_string

    def run(self) -> None:
        tmp_string = self._lcs(D.STRING1, D.STRING2)
        answer = self._lcs(tmp_string, D.STRING3)
        print(len(answer))


if __name__ == '__main__':
    input = open('./1958.txt')
    P = P()
    P.run()