"""
    Solution code for "BaekJoon 미네랄".

    - Problem link: https://www.acmicpc.net/problem/2933
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
# input = open('./2933.txt')


class M:
    """ 이동하기 """
    GO = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


class D:
    ROW = 0
    COL = 0
    board = []
    visited = []
    CUT_COUNT = 0

    # 미네랄 방향
    # 왼쪽 True
    # 오른쪽 False
    CUT_DIRECTION = True

    MINELRAL = "x"
    GROUND = "."

    @staticmethod
    def init_vistied():
        """ 방문 초기화하기 """
        D.visited = [[False] * D.COL for _ in range(D.ROW)]

    @staticmethod
    def show_board(board):
        """ 판 보여주기 """
        for row in board:
            print("".join(row))

class P:

    def __init__(self):
        """ 데이터 받기 """
        D.ROW, D.COL = map(int, input.readline().split())
        D.board = [list(input.readline().strip()) for _ in range(D.ROW)]
        D.CUT_COUNT = int(input.readline())
        D.CUT_LIST = list(map(lambda x: D.ROW - int(x),
                              list(input.readline().strip().split())))

    def _cut_mineral(self, row):
        """ 미네랄 부수기 """
        if D.CUT_DIRECTION: # 왼쪽
            D.CUT_DIRECTION = False
            for col in range(D.COL):
                if D.board[row][col] == D.MINELRAL:
                    D.board[row][col] = D.GROUND
                    return True

        else: # 오른쪽
            D.CUT_DIRECTION = True
            for col in range(D.COL - 1, -1, -1):
                if D.board[row][col] == D.MINELRAL:
                    D.board[row][col] = D.GROUND
                    return True

        # 안부숨
        return False

    def _not_falling_mineral(self):
        """ 떨어지지 않는 미네랄 방문 """
        ground = D.ROW - 1
        for col in range(D.COL):
            if D.board[ground][col] == D.GROUND:
                D.visited[ground][col] = True
                continue

            # 방문 처리
            if D.visited[ground][col]:
                continue

            q = deque([(ground, col)])
            while q:
                crow, ccol = q.popleft()
                if D.visited[crow][ccol]:
                    continue
                D.visited[crow][ccol] = True

                for trow, tcol in M.GO:
                    nrow, ncol = crow + trow, ccol + tcol
                    if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                        continue
                    if D.board[nrow][ncol] == D.GROUND:
                        continue

                    q.append((nrow, ncol))

    def _check_falling_distance(self, start_row, col):
        """ 떨어질 거리 확인하기  """
        count = 0
        for row in range(start_row + 1, D.ROW):
            if D.board[row][col] == D.MINELRAL:
                break
            count += 1
        return count

    def _check_falling_minerals(self):
        """ 떨어져야 하는 미네랄 체크하기 """
        falling_minerals = []
        falling_distance = 0
        for row in range(D.ROW - 1, -1, -1):
            for col in range(D.COL):
                if D.visited[row][col]:
                    continue # 이미 방문한 곳
                elif D.board[row][col] == D.GROUND:
                    D.visited[row][col] = True
                    continue # 빈 공간인 경우

                # 미네랄 만난경우
                elif D.board[row][col] == D.MINELRAL:
                    D.visited[row][col] = True
                    D.board[row][col] = D.GROUND
                    if (count := self._check_falling_distance(row, col)):
                        if not falling_distance:
                            falling_distance = count
                        else:
                            falling_distance = min(falling_distance, count)
                    falling_minerals.append((row, col))

        return falling_distance, falling_minerals

    def _moving_menerals(self, falling_distance, falling_minerals):
        """ 미네랄 이동하기 """
        for row, col in falling_minerals:
            move_row = row + falling_distance
            D.board[move_row][col] = D.MINELRAL

    def run(self) -> None:
        """ 실행 """
        for i, height in enumerate(D.CUT_LIST):
            D.init_vistied()

            # 미네랄 부수기
            if not self._cut_mineral(height):
                continue # 안부순 경우

            # 지탱 받고 있는 미네랄 방문처리
            self._not_falling_mineral()

            # 떨어저야 하는 높이 구하기

            falling_distance, falling_minerals  = self._check_falling_minerals()
            if not falling_distance:
                continue

            # 이동하기
            self._moving_menerals(falling_distance, falling_minerals)

        D.show_board(D.board)


if __name__ == '__main__':
    P = P()
    P.run()