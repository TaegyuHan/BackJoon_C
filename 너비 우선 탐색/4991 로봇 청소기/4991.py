"""
    Solution code for "BaekJoon 로봇 청소기".

    - Problem link: https://www.acmicpc.net/problem/4991
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
# input = open('./4991.txt')


class M:
    """ 이동하기 """
    GO = [
        (0, -1),
        (0, 1),
        (1, 0),
        (-1, 0),
    ]


class D:
    """ 데이터 """
    ROW = 0
    COL = 0
    board = []
    vistied = []

    cleaner_row = 0
    cleaner_col = 0

    dust_count = 0
    dust_break = 0

    CLEANER = "o"
    WALL = "x"
    DUST = "*"

    @staticmethod
    def input_board():
        """ 보드 데이터 받기 """
        D.board = []
        D.dust_count = 0
        for row in range(D.ROW):
            tmp = list(input.readline().strip())
            for col in range(D.COL):
                if tmp[col] == D.CLEANER:
                    D.cleaner_row, D.cleaner_col = row, col
                elif tmp[col] == D.DUST:
                    tmp[col] = 2 ** D.dust_count
                    D.dust_count += 1

            D.board.append(tmp)
        D.dust_break = 2 ** D.dust_count - 1

    @staticmethod
    def init_vistied():
        """ 방문 처리 초기화 """
        D.visited = [[[False] * D.COL
                     for _ in range(D.ROW)]
                     for _ in range(2**D.dust_count)]

    @staticmethod
    def input_row_or_col():
        """ 데이터 받기 """
        D.COL, D.ROW = map(int, input.readline().strip().split())
        return D.ROW and D.COL

    @staticmethod
    def show_board(board):
        """ 판 보여주기 """
        for row in board:
            print(*row)
        print()

    @staticmethod
    def dust_update(dust, state):
        """ 먼지 업데트 """
        return dust | state


class P:

    def _BFS(self):
        """ BFS 알고리즘 적용 """
        move_count = 0
        dusts = 0
        q = deque([(D.cleaner_row,
                    D.cleaner_col,
                    move_count,
                    dusts)])

        while q:
            crow, ccol, cmove, cdust = q.popleft()
            if D.visited[cdust][crow][ccol]: continue
            D.visited[cdust][crow][ccol] = True

            if cdust == D.dust_break:
                print(cmove)
                return

            for trow, tcol in M.GO:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                    continue # 판 검사하기
                if (state := D.board[nrow][ncol]) == D.WALL:
                    continue # 벽 검사하기
                    print(nrow, ncol)
                if isinstance(state, int) and (ndust := D.dust_update(cdust, state)):
                    q.append((nrow, ncol, cmove + 1, ndust))
                    continue # 먼지 일 경우
                q.append((nrow, ncol, cmove + 1, cdust))

        print(-1)

    def run(self) -> None:
        while D.input_row_or_col():
            D.input_board()
            D.init_vistied()
            self._BFS()


if __name__ == '__main__':
    P = P()
    P.run()
