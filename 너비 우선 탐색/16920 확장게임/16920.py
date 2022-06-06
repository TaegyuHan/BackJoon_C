"""
    Solution code for "BaekJoon 확장게임".

    - Problem link: https://www.acmicpc.net/problem/16920
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
input = open('./16920.txt')


class M:
    """ 이동하기 """
    GO = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


class D:
    """ 데이터 """
    ROW = 0
    COL = 0
    CASTLE_COUNT = 0
    MOVING_VALUES = [0]
    ground = []
    castle_deque = [0]
    answer_count = [0]

    GROUND = "."

    @staticmethod
    def show_ground():
        """ 땅 보주기 """
        for row in D.ground:
            print(*row)

class P:

    def __init__(self) -> None:
        """ 데이터 받기 """
        D.ROW, D.COL, D.CASTLE_COUNT = map(int, input.readline().split())
        D.MOVING_VALUES += list(map(int, input.readline().split()))
        D.castle_deque += [deque([]) for _ in range(D.CASTLE_COUNT)]
        D.answer_count += [0 for _ in range(D.CASTLE_COUNT)]

        # 땅 데이터 받기
        for row in range(D.ROW):
            row_tmp = list(input.readline().strip())
            D.ground.append(row_tmp)
            for col in range(D.COL):
                if row_tmp[col].isdigit():
                    D.castle_deque[int(row_tmp[col])].append((row, col, 0))

    def _bfs(self, castle_number: int):
        """ BFS 이용해서 이동하기 """
        tmp_queue = deque([])
        q = D.castle_deque[castle_number]
        change_group = str(castle_number)

        while q:
            crow, ccol, ccount = q.popleft()

            if D.ground[crow][ccol] != D.GROUND and ccount != 0:
                continue

            D.ground[crow][ccol] = change_group

            if ccount >= D.MOVING_VALUES[castle_number]:
                tmp_queue.append((crow, ccol, 0))
                continue

            for trow, tcol in M.GO:
                nrow, ncol = crow + trow, ccol + tcol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                    continue
                if D.ground[nrow][ncol] != D.GROUND:
                    continue
                q.append((nrow, ncol, ccount + 1))

        D.castle_deque[castle_number] = tmp_queue

    def answer_check(self):
        """ 정답 수 구하기 """
        for row in range(D.ROW):
            for col in range(D.COL):
                if D.ground[row][col].isdigit():
                    D.answer_count[int(D.ground[row][col])] += 1

    def run(self) -> None:
        while_break = True

        while while_break:
            while_break = False

            for castle_number in range(1, D.CASTLE_COUNT + 1):
                if D.castle_deque[castle_number]: # 캐슬 움직일 곳이 남아있음
                    self._bfs(castle_number)
                    while_break = True

        self.answer_check()
        print(*D.answer_count[1:])

if __name__ == '__main__':
    P = P()
    P.run()