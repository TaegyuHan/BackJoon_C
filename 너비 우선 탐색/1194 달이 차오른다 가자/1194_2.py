"""
    Solution code for "BaekJoon 달이 차오른다 가자".

    - Problem link: https://www.acmicpc.net/problem/1194
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
# input = open('./1194.txt')


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
    ROW, COL = map(int, input.readline().split())
    board = []
    visited = []

    start_row = 0
    start_col = 0

    ME = "0"
    WALL = "#"
    GROUND = "."
    EXIT = "1"

    KEYS = {
        "a": 1,
        "b": 2,
        "c": 4,
        "d": 8,
        "e": 16,
        "f": 32
    }

    @staticmethod
    def input_board():
        """ 보드 데이터 받기 """
        for row in range(D.ROW):
            tmp = list(input.readline().strip())
            D.board.append(tmp)
            for col in range(D.COL):
                if tmp[col] != D.ME: continue
                D.start_row, D.start_col = row, col

    @staticmethod
    def init_vistied():
        """ 방문처리 생성 """
        D.visited = [[[False] * D.COL for _ in range(D.ROW)] for _ in range(64)]

    @staticmethod
    def update_key(current_key: int, input_key: int) -> int:
        """ 키 업데이트 해주기 """
        return current_key | D.KEYS[input_key]

    @staticmethod
    def check_key(keys: int, door: str) -> bool:
        """ 문 열쇠 존재 확인하기 """
        if D.KEYS[door.lower()] & keys:
            return False # 열쇠 존재 함
        return True # 열쇠 존재 안함

    @staticmethod
    def show_board(board: list[list[int]]):
        """ 판 보여주기 """
        for row in board:
            print(*row)
        print()


class P:

    def __init__(self) -> None:
        """ 데이터 받기 """
        D.input_board()
        D.init_vistied()

    def _BFS(self) -> None:
        """ BFS로 이동 """
        move_count = 0
        key_count = 0
        q = deque([(D.start_row,
                    D.start_col,
                    move_count,
                    key_count)])

        while q:
            crow, ccol, cmove, ckey = q.popleft()
            if D.visited[ckey][crow][ccol]: continue
            D.visited[ckey][crow][ccol] = True

            # 출구 만남
            if D.board[crow][ccol] == D.EXIT:
                print(cmove)
                exit()

            for trow, tcol in M.GO:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                    continue # 판 크기
                if (state := D.board[nrow][ncol]) == D.WALL:
                    continue # 벽 판별하기
                if state.islower() and (nkey := D.update_key(ckey, state)):
                    q.append((nrow, ncol, cmove + 1, nkey))
                    continue  # 키를 먹은 경우
                if state.isupper() and D.check_key(ckey, state):
                    continue # 문을 만난경우
                q.append((nrow, ncol, cmove + 1, ckey))
        
        # 출구 못찾음
        print(-1)

    def run(self) -> None:
        self._BFS()


if __name__ == '__main__':
    P = P()
    P.run()