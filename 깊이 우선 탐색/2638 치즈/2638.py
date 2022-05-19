"""
    Solution code for "BaekJoon 치즈".

    - Problem link: https://www.acmicpc.net/problem/2638
"""
from sys import stdin as input
# import sys; sys.setrecursionlimit(2500)
# input = open('./2638.txt')


class M:
    """ 이동하기 """
    ALL = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


class D:
    """ 데이터 """
    ROW, COL = map(int, input.readline().split())
    board = []
    visited = []

    @staticmethod
    def input_board():
        """ 판 데이터 받기 """
        D.board = [list(map(int, input.readline().split())) for _ in range(D.ROW)]


class P:

    def _show_visited_board(self):
        """ 방문 처리 확인하기 """
        for row in D.visited:
            print(*row)
        print()

    def _show_board(self):
        """ 치즈 확인하기 """
        for row in D.board:
            print(*row)
        print()

    def _reset_visited(self): # 100x100 = 10_000
        """ 방문 처리 초기화 """
        D.visited = [[1] * D.COL for _ in range(D.ROW)]

    def _edge_check(self):
        """ 가장자리 확인 """
        self._reset_visited()
        stack = [(0, 0)]
        cheese_check = False
        while stack:
            crow, ccol = stack.pop()
            if not D.visited[crow][ccol]: continue
            D.visited[crow][ccol] = 0

            for trow, tcol in M.ALL:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL): continue
                if not D.visited[nrow][ncol]: continue
                if D.board[nrow][ncol] == 1:
                    cheese_check = True
                    continue
                stack.append((nrow, ncol))

        return cheese_check

    def _melt_check(self, row, col):
        """ 녹는지 확인하기 """
        count = 0
        for trow, tcol in M.ALL:
            nrow, ncol = trow + row, tcol + col
            if D.visited[nrow][ncol] == 0: count += 1
            if count >= 2: return True
        return False

    def _melting_cheese(self, row, col):
        """ 치즈 녹이기 """
        if not D.board[row][col]: return # 치즈가 아닌경우
        if self._melt_check(row, col): # 치즈 녹음
            D.board[row][col] = 0
            return

    def _find_chees(self):
        """ 치즈 찾기 """
        for row in range(D.ROW):
            for col in range(D.COL):
                if not D.visited[row][col]: continue
                self._melting_cheese(row, col)

    def run(self) -> None:
        D.input_board()
        answer = 0
        while self._edge_check():
            self._find_chees()
            answer += 1
        print(answer)


if __name__ == '__main__':
    P = P()
    P.run()












