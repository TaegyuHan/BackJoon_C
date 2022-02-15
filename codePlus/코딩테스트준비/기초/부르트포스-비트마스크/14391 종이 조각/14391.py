"""Solution code for "BaekJoon 종이 조각".

- Problem link: https://www.acmicpc.net/problem/14391
"""
import sys
from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N, self.M = map(int, input.readline().split())
        self.board = [list(input.readline().strip())
                      for _ in range(self.N)]
        self.length = self.N * self.M
        self.answer = -sys.maxsize

    def _sum_board(self, row: int, col: int) -> int:

        tmp_num = ""
        tmp_bit = self.bits[row][col]

        while self.chcek[row][col] and self.bits[row][col] == tmp_bit:
            self.chcek[row][col] = False
            tmp_num += self.board[row][col]

            if tmp_bit == "0":
                col += 1
                if col == self.M: break

            elif tmp_bit == "1":
                row += 1
                if row == self.N: break

        return int(tmp_num)

    def _check_sum(self, bits: str) -> None:
        sum_val = 0
        self.chcek = [[True for _ in range(self.M)]
                       for _ in range(self.N)]

        back, self.bits = 0, []
        for i in range(0, self.N * self.M + 1, self.M):
            if i == 0: continue
            self.bits.append(list(bits[back:i]))
            back += self.M

        for row in range(self.N):
            for col in range(self.M):
                if self.chcek[row][col]:
                    sum_val += self._sum_board(row, col)
        self.answer = max(self.answer, sum_val)

    def _DFS(self, index: int, bits: str) -> None:
        if index == self.length:
            self._check_sum(bits)
            return True

        self._DFS(index + 1, bits + '0')
        self._DFS(index + 1, bits + '1')

    def result(self) -> None:
        self._DFS(index=0, bits="")
        print(self.answer)

if __name__ == '__main__':
    # input = open('./14391.txt')
    P = P()
    P.result()