"""
    Solution code for "BaekJoon 곡예 비행".

    - Problem link: https://www.acmicpc.net/problem/21923
"""
from sys import stdin as input

input = open('21923.txt')

# data input
MOVE_TYPE_COUNT = 2
UP = 0
DOWN = 1
ROW, COL = map(int, input.readline().split())
ROW_END_INDEX = ROW - 1
COL_END_INDEX = COL - 1
point_board = [list(map(int, input.readline().split())) for _ in range(ROW)]
DP = [[0] * COL for _ in range(ROW)]


def DP_run() -> None:
    for row in range(ROW_END_INDEX, -1, -1):
        for col in range(COL):
            cpoint = point_board[row][col]
            brow, bcol = row + 1, col - 1
            down, left = 0, 0

            if brow <= ROW_END_INDEX:
                down = DP[brow][col]
            if 0 <= bcol:
                left = DP[row][bcol]

            DP[row][col] = max(down + cpoint, left + cpoint)

    for row in range(ROW):
        for col in range(COL):
            cpoint = point_board[row][col]
            brow, bcol = row - 1, col - 1
            up, left = cpoint, cpoint

            if brow <= ROW_END_INDEX:
                up = DP[brow][col]
            if 0 <= bcol:
                left = DP[row][bcol]

            DP[row][col] = max(up + cpoint,
                               left + cpoint,
                               DP[row][col] + cpoint)


def answer() -> None:
    print(DP[ROW_END_INDEX][COL_END_INDEX])


def main() -> None:
    """ 실행 메인 함수 """
    DP_run()
    answer()


if __name__ == '__main__':
    main()