"""
    Solution code for "BaekJoon 성곽".

    - Problem link: https://www.acmicpc.net/problem/2234
"""
from sys import stdin as input
from collections import deque


class S:
    """ 상태 """
    NOT_CHECK = 0
    ROUND = 4


class G:
    """ MOVE """
    MOVE = [
        (0, -1),
        (-1, 0),
        (0, 1),
        (1, 0)
    ]


class D:
    """ data """
    ROW: int
    COL: int
    BOARD: list[str]
    BOARD_CHECK: list[int]
    GROUND_SIZE: list[int]
    LINK = list[set[int]]
    ANSWER1: int
    ANSWER2: int
    ANSWER3: int

class P:

    def __init__(self) -> None:
        D.COL, D.ROW = map(int, input.readline().split())
        D.BOARD = [input.readline().split() for _ in range(D.ROW)]
        D.BOARD_CHECK = [[S.NOT_CHECK for _ in range(D.COL)] for _ in range(D.ROW)]

    def _show_check_board(self):
        """ 보드 확인 시각화 """
        for row in D.BOARD_CHECK:
            print(*row)

    def _bfs(self, row, col, ground_count):
        """ BFS 시작 """
        D.LINK.append(set())
        ground_size = 0
        d = deque([(row, col)])

        while d:
            crow, ccol = d.popleft()
            if D.BOARD_CHECK[crow][ccol] != S.NOT_CHECK: continue
            D.BOARD_CHECK[crow][ccol] = ground_count
            ground_size += 1

            for shift in range(S.ROUND):
                trow, tcol = G.MOVE[shift]
                nrow, ncol = trow + crow, tcol + ccol

                # 벽사이에 존재하는 다른 구간 링크 생성
                if (0 <= nrow < D.ROW and 0 <= ncol < D.COL)\
                    and (D.BOARD_CHECK[crow][ccol] != D.BOARD_CHECK[nrow][ncol])\
                    and D.BOARD_CHECK[nrow][ncol] != S.NOT_CHECK:
                    D.LINK[ground_count].add(D.BOARD_CHECK[nrow][ncol])

                # 움직일 수 있나 확인
                if not int(D.BOARD[crow][ccol]) & (0b1 << shift):
                    d.append((nrow, ncol)) # 움직임

        D.GROUND_SIZE.append(ground_size)
        return ground_size

    def _bfs_find_start_position(self):
        """ 우선 너비 탐색 시작 """
        ground_count = 0
        ground_max_size = 0
        D.GROUND_SIZE = [0]
        D.LINK = [set()]

        for row in range(D.ROW):
            for col in range(D.COL):
                if D.BOARD_CHECK[row][col] != S.NOT_CHECK: continue
                ground_count += 1
                ground_max_size = max(ground_max_size,
                                      self._bfs(row, col, ground_count))

        D.ANSWER1 = ground_count
        D.ANSWER2 = ground_max_size

    def _find_break_wall_max_size(self):
        """ 벽 부수고 최대값 찾기 """
        D.ANSWER3 = 0
        for gorund1, gorunds in enumerate(D.LINK):
            for gorund2 in gorunds:
                D.ANSWER3 = max(D.ANSWER3,
                                D.GROUND_SIZE[gorund1] + D.GROUND_SIZE[gorund2])

    def _show_answer(self):
        """ 정답  """
        print(D.ANSWER1)
        print(D.ANSWER2)
        print(D.ANSWER3)

    def run(self) -> None:
        self._bfs_find_start_position()
        self._find_break_wall_max_size()
        self._show_answer()

if __name__ == '__main__':
    # input = open('./2234.txt')
    P = P()
    P.run()