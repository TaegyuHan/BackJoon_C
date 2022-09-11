"""
    Solution code for "BaekJoon 곡예 비행".

    - Problem link: https://www.acmicpc.net/problem/21923
"""
from sys import stdin as input
from sys import maxsize
# input = open('21923.txt')

# data input
ROW, COL = map(int, input.readline().split())
ROW_END_INDEX = ROW - 1
COL_END_INDEX = COL - 1
point_board = [list(map(int, input.readline().split())) for _ in range(ROW)]
DP = [[0] * COL for _ in range(ROW)]


def airplane_up() -> None:
    """ 비행기 상승 DP """
    for row in range(ROW_END_INDEX, -1, -1):
        for col in range(COL):
            cpoint = point_board[row][col]
            if row == ROW_END_INDEX and col == 0:
                DP[row][col] = cpoint
                continue
            brow, bcol = row + 1, col - 1
            down, left = -maxsize, -maxsize

            # 아래
            if brow <= ROW_END_INDEX:
                down = DP[brow][col]

            # 왼쪽
            if 0 <= bcol:
                left = DP[row][bcol]

            DP[row][col] = max(cpoint + down, cpoint + left)


def airplane_down() -> None:
    """ 비행기 하강 DP """
    for row in range(ROW):
        for col in range(COL):
            cpoint = point_board[row][col]
            brow, bcol = row - 1, col - 1
            up, left = cpoint, cpoint

            # 위
            if brow <= ROW_END_INDEX:
                up = DP[brow][col]

            # 왼쪽
            if 0 <= bcol:
                left = DP[row][bcol]

            DP[row][col] = max(up + cpoint,
                               left + cpoint,
                               DP[row][col] + cpoint)


def DP_run() -> None:
    """ DP 채우기 """
    airplane_up()
    # show_dp
    airplane_down()
    # show_dp


def show_dp() -> None:
    """ dp 확인하기 """
    for row in DP:
        print(*row)


def answer() -> None:
    print(DP[ROW_END_INDEX][COL_END_INDEX])


def main() -> None:
    """ 실행 메인 함수 """
    DP_run()
    answer()


if __name__ == '__main__':
    main()
