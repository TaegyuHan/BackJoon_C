"""
    Solution code for "BaekJoon 로봇 청소기".

    - Problem link: https://www.acmicpc.net/problem/14503
"""

from sys import stdin as input


class M:
    """ 이동 """
    ALL = [
        (-1, 0), # 북
        (0, 1), # 동
        (1, 0), # 남
        (0, -1), # 서
    ]


class S:
    """ 상태 """
    NO_CLEAN = False
    CLEAN = True
    BREAK = 4
    WALL = 1


class C:
    row: int
    col: int
    direction: int
    count = 0
    break_count = 0
    _turn = [3, 0, 1, 2]

    @staticmethod
    def clean():
        C.count += 1

    @staticmethod
    def turn():
        """ 돌기 """
        move = C._turn[C.direction]
        nrow, ncol = M.ALL[move][0] + C.row, M.ALL[move][1] + C.col
        if not (0 <= nrow < B.ROW and 0 <= ncol < B.COL): return False
        if B.board[nrow][ncol] == S.WALL: return False
        if B.visited[nrow][ncol]: return False
        # 이동 가능
        return True

    @staticmethod
    def turn_move(row, col):
        """ 이동하기 """
        B.visited[row][col] = True
        C.row, C.col = row, col

    @staticmethod
    def move_a():
        turn_count = 0
        while turn_count < 4:
            if C.turn(): # 이동
                return
            turn_count += 1

class B:
    """ 판 """
    ROW: int
    COL: int
    board: list[list[int]]
    visited: list[list[int]]

    @staticmethod
    def show_board():
        for row in B.board:
            print(*row)
        print()

class P:

    def __init__(self) -> None:
        B.ROW, B.COL = map(int, input.readline().split())
        C.row, C.col, C.direction = map(int, input.readline().split())
        B.board = [list(map(int, input.readline().split())) for _ in range(B.ROW)]
        B.visited = [[False for _ in range(B.COL)] for _ in range(B.ROW)]

    def run(self) -> None:
        while True:
            C.clean() # 청소 1번
            C.move_a()
            break

        print(C.count)


if __name__ == '__main__':
    input = open('./14503.txt')
    P = P()
    P.run()
