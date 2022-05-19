"""
    Solution code for "BaekJoon 빵집".

    - Problem link: https://www.acmicpc.net/problem/3109
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./3109.txt')


class M:
    """ 파이프 이동 """
    GO = [
        (-1, 1),
        (0, 1),
        (1, 1),
    ]


class D:
    """ 데이터 """
    ROW, COL = map(int, input.readline().split())
    WALL = "x"
    SUCCESS = 1
    FAIL = 0
    board = []
    vistied = []

    @staticmethod
    def INPUT_MAP():
        """ 맵 데이터 받기 """
        D.board = [list(input.readline()) for _ in range(D.ROW)]

    @staticmethod
    def visteid_init():
        """ 방문처리 초기화 """
        D.vistied = [[False] * D.COL for _ in range(D.ROW)]

    @staticmethod
    def show_map():
        """ 맵 확인하기 """
        for row in D.board:
            print(*row)
        print()

    @staticmethod
    def show_visited():
        """ 방문처리 확인하기 """
        for row in D.vistied:
            print(*row)
        print()


class P:

    def _connect_success(self, visted):
        """ 연동 성공 """
        for row, col in visted:
            D.vistied[row][col] = True

    def _DFS(self, row, col, visted):
        """ 우선 깊이 탐색 파이프 연동 """
        if col == D.COL - 1: # 연동 성공
            self._connect_success(visted)
            return D.SUCCESS

        for trow, tcol in M.GO:
            nrow, ncol = trow + row, tcol + col
            if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL): continue
            if D.board[nrow][ncol] == D.WALL: continue
            if D.vistied[nrow][ncol]: continue
            if self._DFS(nrow, ncol, visted + [(nrow, ncol)]):
                return D.SUCCESS
            D.vistied[nrow][ncol] = True

        return D.FAIL

    def _connecting(self):
        """ 가스 파이프 연동 """
        answer = 0
        for row in range(D.ROW):
            answer += self._DFS(row, col=0, visted=[(row, 0)])
        print(answer)

    def run(self) -> None:
        D.INPUT_MAP()
        D.visteid_init()
        self._connecting()


if __name__ == '__main__':
    P = P()
    P.run()
