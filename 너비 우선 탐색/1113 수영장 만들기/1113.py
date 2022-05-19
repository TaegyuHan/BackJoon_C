"""Solution code for "BaekJoon 수영장 만들기".

- Problem link: https://www.acmicpc.net/problem/1113
"""
from sys import stdin as input
from sys import maxsize
from collections import deque
input = open('./1113.txt')


class M:
    """ 이동 """
    ALL = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


class D:
    """ 데이터  """
    ROW, COL = map(int, input.readline().split())
    BOARD = [] # 판 데이터
    visited = [] # 방문처리
    answer = 0

    @staticmethod
    def INPUT_BOARD():
        """ 보드 받기 """
        D.BOARD = [list(map(int, list(input.readline().strip()))) for _ in range(D.ROW)]

    @staticmethod
    def make_visited():
        """ 방문 처리 만들기  """
        D.visited = [[False] * D.COL for _ in range(D.ROW)]


class P:

    def _show_board(self):
        """ 판 보여주기 """
        for row in D.BOARD:
            print(*row)

    def _show_visited_board(self):
        """ 방문처리 판 보여주기 """
        for row in D.visited:
            print(*row)

    def _max_min_check(self): # +2500
        """ 보드 최대 최소 반환 함수 """
        maximum = 0
        minimum = maxsize
        for row in range(D.ROW):
            for col in range(D.COL):
                if D.BOARD[row][col] > maximum:
                    maximum = D.BOARD[row][col]
                if D.BOARD[row][col] < minimum:
                    minimum = D.BOARD[row][col]

        return minimum, maximum

    def _fill_bfs(self, row, col, height):
        """ 채우는 BFS

            물을 채우는 방문처리
        """
        fill_count = 0
        if D.BOARD[row][col] > height: # 크기 확인
            D.visited[row][col] = True
            return fill_count

        q = deque([(row, col)])
        while q:
            crow, ccol = q.popleft()
            if D.visited[crow][ccol]: continue # 방문 처리
            D.visited[crow][ccol] = True
            fill_count += 1

            for trow, tcol in M.ALL:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL): continue # 배열 범위
                if D.BOARD[nrow][ncol] > height: continue
                q.append((nrow, ncol))

        return fill_count

    def _filling_with_water(self, height):
        """ 물채우기 """
        D.make_visited() # 새로운 방문 처리 # x2500
        fill_count = 0

        # 가장자리 확인하기
        for row in range(D.ROW): # x50
            if row in (0, D.ROW - 1): # 맨위, 맨 아래
                col_range = range(D.COL)
            else: # 사이드
                col_range = (0, D.COL - 1)

            for col in col_range:
                if D.visited[row][col]: continue # 방문 확인
                self._fill_bfs(row, col, height)

        # 채울 곳 확인하기
        for row in range(1, D.ROW - 1): # x48
            for col in range(1, D.COL - 1): # 48
                if D.visited[row][col]: continue  # 방문 확인
                fill_count += self._fill_bfs(row, col, height)
        return fill_count

    def _run_check(self):
        """ 실행 확인 """
        if D.ROW < 3 or D.COL < 3:
            print(0)
            exit()

    def run(self) -> None:
        D.INPUT_BOARD()
        self._run_check()
        minimum, maximum = self._max_min_check() # +2500
        for height in range(minimum , maximum + 1): # x9
            D.answer += self._filling_with_water(height) # x5000

        print(D.answer)

if __name__ == '__main__':
    P = P()
    P.run()