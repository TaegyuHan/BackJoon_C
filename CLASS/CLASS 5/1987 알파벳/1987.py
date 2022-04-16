"""
    Solution code for "BaekJoon 알파벳".

    - Problem link: https://www.acmicpc.net/problem/1987
"""


from sys import stdin as input


class D:
    """ 데이터 """
    ROW: int
    COL: int
    BOARD = []
    CHECK = []
    ALPHABET_COUNT = 26
    ANSWER = 0


class G:
    """ Go 방향 """
    MOVE = [
        (-1, 0), # 위
        (0, 1), # 오른쪽
        (1, 0), # 아래
        (0, -1)  # 왼쪽
    ]


def num(char):
    """ 알파벳 숫자로 변경 """
    return ord(char) - 65


class P:

    def __init__(self) -> None:
        D.ROW, D.COL = map(int, input.readline().split())
        D.BOARD = [list(input.readline().strip()) for _ in range(D.ROW)]
        D.CHECK = [False for _ in range(D.ALPHABET_COUNT)]

    def _DFS(self, row, col, count):
        """ 우선 깊이 탐색 """
        alphabet_num = num(D.BOARD[row][col])
        # 기존에 들렸던 알파벳 리턴
        if D.CHECK[alphabet_num]:
            if D.ANSWER < count:
                D.ANSWER = count
            return

        D.CHECK[alphabet_num] = True
        for trow, tcol in G.MOVE:
            nrow, ncol = trow + row, tcol + col
            if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL): continue
            self._DFS(nrow, ncol, count + 1)

        D.CHECK[alphabet_num] = False

    def run(self) -> None:
        """ 실행 """
        self._DFS(row=0, col=0, count=0)
        print(D.ANSWER)


if __name__ == '__main__':
    # input = open('./1987.txt')
    P = P()
    P.run()