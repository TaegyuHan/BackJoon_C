"""
    Solution code for "BaekJoon 열쇠".

    - Problem link: https://www.acmicpc.net/problem/9328
"""
from sys import stdin as input
from collections import deque


class M:
    ALL = [
        (0, 0),
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]


class D:
    """ 데이터 """
    TEST_CASE: int


class A:
    """ 알파벳 """
    COUNT = 26


class B:
    """ 판 """
    NOT_CHECK = False
    CHECK = True

    FIRST_ROW = 0
    LAST_ROW: int
    FRONT_COL = 0
    BACK_COL: int

    WALL = "*"
    EMPTY = "."
    DOC = "$"

    row: int
    col: int
    answer: int
    keys: set[str]
    board = []
    starts = []


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _input_board(self):
        """ 판 생성하기 """
        B.answer = 0
        B.board = []
        B.starts = []
        B.row, B.col = map(int, input.readline().split())
        B.LAST_ROW, B.BACK_COL = B.row - 1, B.col - 1

        for row in range(B.row):
            row_tmp = list(input.readline().strip())
            B.board.append(row_tmp)

            # 첫줄 마지막 줄 확인
            if row == B.FIRST_ROW or B.LAST_ROW == row:
                for col, door_check in enumerate(row_tmp):
                    if B.WALL == door_check: continue
                    B.starts.append((row, col))
                continue

            # 중간 컬럼 확인
            if B.WALL != row_tmp[B.FRONT_COL]:
                B.starts.append((row, B.FRONT_COL))

            if B.WALL != row_tmp[B.BACK_COL]:
                B.starts.append((row, B.BACK_COL))

        B.keys = set(input.readline().strip())

    def _show_board(self):
        """ 판 보기 """
        for row in B.board:
            print(*row)

    def _bfs(self, start):
        """ 우선 넓이 탐색 """
        visited = [[B.NOT_CHECK for _ in range(B.col)] for _ in range(B.row)]
        row, col = start
        q = deque([(row, col)])

        while q:
            crow, ccol = q.popleft()

            # 방문 했던 곳 제거
            if visited[crow][ccol]: continue
            visited[crow][ccol] = B.CHECK

            # 벽
            if (state := B.board[crow][ccol]) == B.WALL: continue

            # 문 만남
            if B.board[crow][ccol].isupper():
                if B.board[crow][ccol].lower() not in B.keys: continue
                B.board[crow][ccol] = B.EMPTY

            # 문서 만남
            if state == B.DOC:
                B.answer += 1
                B.board[crow][ccol] = B.EMPTY

            # 키 만남
            if state.islower():
                B.board[crow][ccol] = B.EMPTY
                B.keys.add(state)

            for go in M.ALL:
                trow, tcol = go
                nrow, ncol = trow + crow, tcol + ccol

                if not (0 <= nrow < B.row and 0 <= ncol < B.col): continue
                if visited[nrow][ncol]: continue

                q.append((nrow, ncol))

    def _check_document(self):
        """ 문서 확인하기 """
        for _ in range(A.COUNT):
            tmp_key_count = len(B.keys)
            for start in B.starts:
                self._bfs(start)
                # 전과 key의 개수가 같으면 멈추기
            if tmp_key_count == len(B.keys):
                return

    def run(self) -> None:
        for _ in range(D.TEST_CASE):
            self._input_board()
            self._check_document()
            print(B.answer)


if __name__ == '__main__':
    # input = open('./9328.txt')
    P = P()
    P.run()
