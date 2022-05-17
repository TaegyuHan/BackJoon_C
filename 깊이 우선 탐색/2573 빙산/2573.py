"""
    Solution code for "BaekJoon 빙산".

    - Problem link: https://www.acmicpc.net/problem/2573
"""
from sys import stdin as input
# input = open('./2573.txt')


class S:
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class M:
    """ 이동하기 """
    TYPE = [
        (-1, 0), # 아래
        (1, 0), # 위
        (0, -1), # 왼쪽
        (0, 1), # 오른쪽
    ]


class B:
    """ 판 """
    ROW, COL = map(int, input.readline().split())
    board = [list(map(int, input.readline().split())) for _ in range(ROW)]
    copy = [] # 판의 정보
    visited = [] # 방문 처리

    @staticmethod
    def show_board():
        """ 판 보여주기 """
        for row in B.board:
            print(row)
        print()

    @staticmethod
    def DFS(row, col):
        """ 우선 깊이 탐색 """
        B.copy = [row[:] for row in B.board] # deepcopy
        stack = [(row, col)]
        while stack:
            crow, ccol = stack.pop()
            if B.visited[crow][ccol]: continue
            B.visited[crow][ccol] = True
            melting_count = 0
            for trow, tcol in M.TYPE:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < B.ROW and 0 <= ncol < B.COL): continue
                elif B.board[nrow][ncol] == 0:
                    melting_count += 1
                    continue
                elif B.visited[nrow][ncol]: continue
                stack.append((nrow, ncol))
            B.copy[crow][ccol] = \
                max(B.copy[crow][ccol] - melting_count, 0)

        B.board = B.copy
        return 1

    @staticmethod
    def find_ice():
        """ 첫번째 빙산 찾기 """
        B.visited = [[False for _ in range(B.COL)] for _ in range(B.ROW)]
        count = 0
        for row in range(B.ROW):
            for col in range(B.COL):
                if B.visited[row][col]: continue
                if B.board[row][col] == 0:
                    B.visited[row][col] = True
                    continue
                count += B.DFS(row, col)
        return count


class P:

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        time = 0
        while True:
            count = B.find_ice()
            if count == 0:
                print(0)
                break
            if count >= 2:
                print(time)
                break
            time += 1


if __name__ == '__main__':
    P = P()
    P.run()