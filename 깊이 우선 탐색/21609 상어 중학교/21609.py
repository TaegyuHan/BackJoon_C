"""
    Solution code for "BaekJoon 상어 중학교".

    - Problem link: https://www.acmicpc.net/problem/21609
"""
from sys import stdin as input
from collections import deque
import sys;


sys.setrecursionlimit(2500)
# input = open('./21609.txt')


class M:
    """ 확인하기 """
    ALL = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]


class D:
    """ 데이터 """
    N, COLOR = map(int, input.readline().split())

    board = []
    visited = []
    zero_visited = []

    SPACE = -2
    RAINBOW_BLOCK = 0
    BLACK_BLOCK = -1
    NO_GROUP = [RAINBOW_BLOCK, BLACK_BLOCK, SPACE]

    @staticmethod
    def input_board():
        """ 상어 데이터 받기 """
        D.board = [list(map(int, input.readline().split())) for _ in range(D.N)]

    @staticmethod
    def init_visited():
        """ 방문처리 확인 """
        D.visited = [[False] * D.N for _ in range(D.N)]

    @staticmethod
    def init_zero_tvisited():
        """ 방문처리 확인 """
        D.zero_visited = [[False] * D.N for _ in range(D.N)]

    @staticmethod
    def show_board(array_data):
        """ 배열 보여주기 """
        for row in array_data:
            for col in row:
                print(col, end="\t")
            print()
        print()


class P:

    def _BFS(self, row, col):
        """ 너비 우선 탐색 """
        D.init_zero_tvisited()
        shark_type = D.board[row][col]
        q = deque([(row, col)])

        group = {
            "count": 0,
            "zero_count": [],
            "shark_data": []
        }

        while q:
            crow, ccol = q.popleft()
            # 방문 확인
            if D.visited[crow][ccol]: continue
            if D.zero_visited[crow][ccol]: continue
            group["count"] += 1

            # 방문처리
            if D.board[crow][ccol] != D.RAINBOW_BLOCK:
                D.visited[crow][ccol] = True
                group["shark_data"].append((crow, ccol))

            if D.board[crow][ccol] == D.RAINBOW_BLOCK:
                D.zero_visited[crow][ccol] = True
                group["zero_count"].append((crow, ccol))

            # 이동하기
            for trow, tcol in M.ALL:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < D.N and 0 <= ncol < D.N): continue
                if D.board[nrow][ncol] != shark_type and D.board[nrow][ncol] != D.RAINBOW_BLOCK: continue
                q.append((nrow, ncol))

        group["shark_data"].sort(key=lambda x: (x[0], x[1]))

        if not group["count"] or group["count"] == 1:
            return {}
        return group

    def _group_comparison(self, max_group, group):
        """ 상어 그룹 비교 """

        # # 그룹 개수 비교
        if max_group["count"] < group["count"]:
            return group
        elif max_group["count"] > group["count"]:
            return max_group

        # 무지개 블록 확인
        if len(max_group["zero_count"]) < len(group["zero_count"]):
            return group
        elif len(max_group["zero_count"]) > len(group["zero_count"]):
            return max_group

        max_row, max_col = max_group["shark_data"][0]
        row, col = group["shark_data"][0]
        if max_row < row:
            return group
        elif max_row > row:
            return max_group

        if max_col < col:
            return group
        elif max_col > col:
            return max_group

    def _delete_group(self, group):
        """ 상어 삭제 """
        for row, col in group["zero_count"]:
            D.board[row][col] = D.SPACE

        for row, col in group["shark_data"]:
            D.board[row][col] = D.SPACE

    def _make_shark_group(self):
        """ 상어 그룹 만들기 """
        D.init_visited()
        maximum = {}
        for row in range(D.N):
            for col in range(D.N):
                if D.board[row][col] in D.NO_GROUP: continue
                if not (group := self._BFS(row, col)): continue
                if not maximum: # 처음 데이터
                    maximum = group
                    continue
                maximum = self._group_comparison(maximum, group)

        # 상어 그룹 없음
        if not maximum: return 0
        self._delete_group(maximum)
        return maximum["count"]**2

    def _gravity(self):
        """ 중력 적용하기 """

        board_tmp = []
        for col in range(D.N):
            space_tmp = []
            result_tmp = []
            for row in range(D.N - 1, -1, -1):
                # -1 만났을 경우
                if (state := D.board[row][col]) == D.BLACK_BLOCK:
                    result_tmp += space_tmp
                    result_tmp.append(D.BLACK_BLOCK)
                    space_tmp = []
                elif state == D.SPACE:
                    space_tmp.append(D.SPACE)
                else:
                    result_tmp.append(state)

            result_tmp += space_tmp
            board_tmp.append(result_tmp)

        D.board = board_tmp
        self._board_cycle()


    def _board_cycle(self):
        """ 보드 회전시키기 """
        tmp = []
        zip_board = list(zip(*D.board))
        while zip_board:
            tmp.append(list(zip_board.pop()))
        D.board = tmp

    def run(self) -> None:
        D.input_board()
        answer = 0
        count = 0
        while (point := self._make_shark_group()):
            answer += point
            self._gravity()
            self._board_cycle()
            self._gravity()
            count += 1

        print(answer)


if __name__ == '__main__':
    P = P()
    P.run()