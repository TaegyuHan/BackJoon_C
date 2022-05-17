"""
    Solution code for "BaekJoon 욕심쟁이 판다".

    - Problem link: https://www.acmicpc.net/problem/1937
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./1937.txt')


class M:
    """ 이동하기 """
    GO = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]


class D:
    """ 데이터 """
    N = int(input.readline())
    BOARD = [list(map(int, input.readline().split())) for _ in range(N)]
    dp = []
    answer = 0
    count = 0

    @staticmethod
    def make_dp():
        """ DP 기록 들기 """
        D.dp = [[0 for _ in range(D.N)] for _ in range(D.N)] # 2_500


class P:

    def _show_dp(self):
        """ dp 확인하기 """
        for row in D.dp:
            print(*row)

    def _DFS(self, row, col):
        """ 우선 깊이 탐색 """
        if D.dp[row][col]: return D.dp[row][col]
        D.dp[row][col] = 1;

        for trow, tcol in M.GO:
            nrow, ncol = trow + row, tcol + col
            if not (0 <= nrow < D.N and 0 <= ncol < D.N): continue
            if D.BOARD[row][col] >= D.BOARD[nrow][ncol]: continue

            D.dp[row][col] = max(D.dp[row][col],
                                 self._DFS(nrow, ncol) + 1)

        return D.dp[row][col]

    def _find_position(self):
        """ 위치 찾기 """ # 2_500
        for row in range(D.N):
            for col in range(D.N):
                D.answer = max(D.answer, self._DFS(row, col))

    def run(self) -> None:
        """ 실행 """
        D.make_dp()
        self._find_position()
        print(D.answer)


if __name__ == '__main__':
    P = P()
    P.run()