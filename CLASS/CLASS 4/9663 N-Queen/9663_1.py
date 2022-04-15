"""
    Solution code for "BaekJoon N-Queen".

    - Problem link: https://www.acmicpc.net/problem/9663
"""

from sys import stdin as input
from itertools import combinations

class D:
    """ Data """
    N: int

class Move:
    """ 말 움직이기 """
    GO = [
        [-1, -1], # 위 왼쪽
        [-1, 0], # 위 중앙
        [-1, 1], # 위 오른쪽

        [0, -1], # 중앙 왼쪽
        [0, 0], # 중앙 중앙
        [0, 1], # 중앙 오른쪽

        [1, -1], # 아래 왼쪽
        [1, 0], # 아래 중앙
        [1, 1], # 아래 오른쪽
    ]

class P:

    def __init__(self) -> None:
        D.N = int(input.readline())
        self._init_position()

    def _init_position(self):
        """ 말을 놓을 수 있는 경우 """
        position = []
        for row in range(D.N):
            for col in range(D.N):
                position.append((row, col))
        self.position = combinations(position, 3)

    def _move_piece(self, row, col):
        """ 말움직이면서 확인 """

        # 말 하나가 오른쪽 왼쪽 위 아래 로 움직이기
        for go_tmp in range(1, D.N):
            for direction in Move.GO:
                trow, tcol = map(lambda x:x*go_tmp, direction)
                nrow, ncol = trow + row, tcol + col
                if not (0 <= nrow < D.N and 0 <= ncol < D.N): continue
                # print(nrow, ncol)

    def _check_meet(self, case):
        """ 말이 서로 만나는지 확인 """
        self.tmp = set()
        self.tmp_row = set()
        self.tmp_col = set()

        # 만나는지 확인하기 위한 키 저장
        for row_or_col in case:
            row, col = row_or_col
            self.tmp.add(f"{row},{col}")
            if row in self.tmp_row: return # 가로 동일한지 확인
            if col in self.tmp_col: return # 세로 동일한지 확인
            self.tmp_row.add(row)
            self.tmp_col.add(col)

        print(case)
        for row_or_col in case:
            row, col = row_or_col
            self._move_piece(row, col)

    def run(self) -> None:
        for case in self.position:
            self._check_meet(case)

if __name__ == '__main__':
    input = open('./9663.txt')
    P = P()
    P.run()