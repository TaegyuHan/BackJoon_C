"""
    Solution code for "BaekJoon 탈출".

    - Problem link: https://www.acmicpc.net/problem/3055
"""
from sys import stdin as input
from collections import deque


class G:
    """ 이동 """
    LEN = 4
    X = [-1, 1, 0, 0]
    Y = [0, 0, 1, -1]


class M:
    """ 지도 """
    ROW: int
    COL: int

    END_POINT = "D"
    END_ROW: int
    END_COL: int

    BEAVER = "S"
    START_ROW: int
    START_COL: int

    WATER = "*"
    WALL = "X"
    EMPTY = "."

    WATER_BREAK = {END_POINT, WALL}
    BEAVER_BREAK = {WALL, WATER}

    board = []
    visited = []

    water_q = deque([])
    beaver_q = deque([])

    @staticmethod
    def show_board():
        """ 판 보여주기 """
        print(*list(map(" ".join, M.board)), sep="\n")

    @staticmethod
    def show_visited_board():
        """ 판 보여주기 """
        print(*list(M.visited), sep="\n")

    @staticmethod
    def beaver_move_check():
        """ 비버 움직임 확인하기 """
        if M.beaver_q:
            return True
        return False

class P:

    def __init__(self) -> None:
        M.ROW, M.COL = map(int, input.readline().split())
        self._input_data()

    def _input_data(self):
        """ 판 데이터 받기 """
        for row in range(M.ROW):

            tmp = list(input.readline().strip())
            visited_tmp = []

            for col in range(M.COL):
                visited_tmp.append(False)
                if tmp[col] == M.END_POINT:
                    M.END_ROW, M.END_COL = row, col
                elif tmp[col] == M.BEAVER:
                    M.START_ROW, M.START_END = row, col
                    M.beaver_q.append((row, col))
                elif tmp[col] == M.WATER:
                    M.water_q.append((row, col))

            M.board.append(tmp)
            M.visited.append(visited_tmp)

    def _water_bfs(self):
        """ 물 BFS """
        tmp_water = deque([])
        while M.water_q:
            crow, ccol = M.water_q.popleft()
            if M.visited[crow][ccol]: continue
            M.visited[crow][ccol] = True
            M.board[crow][ccol] = M.WATER

            for i in range(G.LEN):
                nrow, ncol = crow + G.X[i], ccol + G.Y[i]
                if not (0 <= nrow < M.ROW and 0 <= ncol < M.COL): continue
                if M.board[nrow][ncol] in M.WATER_BREAK: continue
                if M.visited[nrow][ncol]: continue
                tmp_water.append((nrow, ncol))

        M.water_q = tmp_water

    def _beaver_bfs(self):
        """ 비버 BFS """
        tmp_beaver = deque([])
        while M.beaver_q:
            crow, ccol = M.beaver_q.popleft()
            if M.visited[crow][ccol]: continue
            M.visited[crow][ccol] = True
            if M.board[crow][ccol] == M.END_POINT:
                print(self._count)
                exit()
                return

            M.board[crow][ccol] = M.BEAVER

            for i in range(G.LEN):
                nrow, ncol = crow + G.X[i], ccol + G.Y[i]
                if not (0 <= nrow < M.ROW and 0 <= ncol < M.COL): continue
                if M.board[nrow][ncol] in M.BEAVER_BREAK: continue
                if M.visited[nrow][ncol]: continue
                tmp_beaver.append((nrow, ncol))

        M.beaver_q = tmp_beaver


    def run(self) -> None:
        """ 실행 """
        self._count = 0
        self._water_bfs()

        while M.beaver_move_check():
            self._beaver_bfs()
            self._water_bfs()
            self._count += 1
        print("KAKTUS")


if __name__ == '__main__':
    # input = open('./3055.txt')
    P = P()
    P.run()