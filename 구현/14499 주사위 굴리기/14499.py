"""
    Solution code for "BaekJoon 주사위 굴리기".

    - Problem link: https://www.acmicpc.net/problem/14499
"""
from sys import stdin as input


class D:
    """ 주사위 """
    row: int
    col: int
    moves: list[int]
    map_direction = 1

    # 방향
    EAST = 1
    WEST = 2
    NORTH = 3
    SOUTH = 4
    OPP = 5

    # 지도 이동
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    # 주사위 값
    value = [0,
             0, # 1
             0, # 2
             0, # 3
             0, # 4
             0, # 5
             0] # 6

    # 주사위 이동
    direction = {
        1: {
            EAST: (3, RIGHT),  # 동
            WEST: (4, LEFT),  # 서
            SOUTH: (5, DOWN),  # 남
            NORTH: (2, UP),  # 북
            OPP: 6 # 반대
        },
        2: {
            EAST: (3, RIGHT),  # 동
            WEST: (4, LEFT),  # 서
            SOUTH: (1, DOWN),  # 남
            NORTH: (6, UP),  # 북
            OPP: 5  # 반대
        },
        3: {
            EAST: (6, RIGHT),  # 동
            WEST: (1, LEFT),  # 서
            SOUTH: (5, DOWN),  # 남
            NORTH: (2, UP),  # 북
            OPP: 4  # 반대
        },
        4: {
            EAST: (6, RIGHT),  # 동
            WEST: (1, LEFT),  # 서
            SOUTH: (5, DOWN),  # 남
            NORTH: (2, UP),  # 북
            OPP: 3  # 반대
        },
        5: {
            EAST: (3, RIGHT),  # 동
            WEST: (4, LEFT),  # 서
            SOUTH: (6, DOWN),  # 남
            NORTH: (1, UP),  # 북
            OPP: 2  # 반대
        },
        6: {
            EAST: (3, RIGHT),  # 동
            WEST: (4, LEFT),  # 서
            SOUTH: (2, DOWN),  # 남
            NORTH: (5, UP),  # 북
            OPP: 1  # 반대
        }
    }

    @staticmethod
    def move(direction):
        """ 주사위 움직임 """
        # 주사위 데이터 변경하기
        next_map_direction, (trow, tcol) = D.direction[D.map_direction][direction]
        # print(D.map_direction, D.direction[D.map_direction][direction])
        nrow, ncol = D.row + trow, D.col + tcol

        # 범위 밖으로 나가는 경우
        if not (0 <= nrow < B.ROW and 0 <= ncol < B.COL): return

        # 주사위 이동
        D.row, D.col = nrow, ncol
        D.map_direction = next_map_direction

        # 주사위 값이 0이고 지도 값이 0이 아닌경우
        # 둘이 값 변경
        # print(D.map_direction, D.value[D.map_direction], B.board[nrow][ncol])
        if D.value[D.map_direction] == 0 \
                and B.board[nrow][ncol] != 0:
            D.value[D.map_direction], B.board[nrow][ncol] = \
                B.board[nrow][ncol], D.value[D.map_direction]

        # 주사위 값이 0이 아니고 지도 값이 0인 경우
        elif D.value[D.map_direction] == 0 \
                and B.board[nrow][ncol] != 0:
            D.value[D.map_direction], B.board[nrow][ncol] = \
                B.board[nrow][ncol], D.value[D.map_direction]

        # print(D.value[D.direction[D.map_direction][D.OPP]])

class B:
    """ 판 정보 """
    ROW: int
    COL: int
    board: list[list[int]]

    @staticmethod
    def show_board():
        """ 현재 판 보여주기 """
        for row in B.board:
            print(*row)


class P:

    def __init__(self) -> None:
        B.ROW, B.COL, D.row, D.col, move_count = \
            map(int, input.readline().split())
        # 판 데이터 넣기
        self._init_board()
        # 움직임 넣기
        D.moves = list(map(int, input.readline().split()))

    def _init_board(self):
        """ 판 데이터 넣기 """
        B.board = [[0 for _ in range(B.COL)] for _ in range(B.ROW)]
        for row in range(B.ROW):
            tmp = list(map(int, input.readline().split()))
            for col in range(B.COL):
                B.board[row][col] = tmp[col]

    def run(self) -> None:
        for i, move_num in enumerate(D.moves):
            D.move(move_num)
            print(D.map_direction)


if __name__ == '__main__':
    input = open('./14499.txt')
    P = P()
    P.run()