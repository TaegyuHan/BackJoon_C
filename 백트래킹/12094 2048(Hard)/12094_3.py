"""
    Solution code for "BaekJoon 2048 (Hard)".

    - Problem link: https://www.acmicpc.net/problem/12094
"""

from sys import stdin as input
# input = open('./12094.txt')


class S:
    """  """
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class B:
    """ 보드판 """
    N = int(input.readline())
    B = []
    MOVE = 4

    BREAK = 10
    SUM = 0
    max_check = [0] * (BREAK + 1)
    largest = 0
    pow_2 = [2**i for i in range(21)]

    @staticmethod
    def input_board():
        for _ in range(B.N):
            row = list(map(int, input.readline().strip().split()))
            B.SUM += sum(row)
            B.B.append(row)

    @staticmethod
    def show_board():
        """ 판 확인하기 """
        for row in B.B:
            print(row)
        print()

class P:

    def __init__(self):
        """ 데이터 받기 """
        B.input_board()

    def _BT(self, deep):
        """ 백트래킹 """
        if deep > B.BREAK:
            if B.largest == B.max_check[B.BREAK]:
                print(B.largest)
                exit()
            return

        for move_type in range(B.MOVE):
            copy = [row[:] for row in B.B]
            tmax = self._move(move_type)
            B.max_check[deep] = max(B.max_check[deep], tmax)

            if B.B != copy \
                    and (B.max_check[B.BREAK] == 0 \
                         or tmax * B.pow_2[B.BREAK - (deep)] > B.max_check[B.BREAK]):
                self._BT(deep + 1)
            B.B = copy

    def _move(self, move_type):
        """ 판 움직이기 """
        max_num = 0

        if move_type == S.UP:
            for col in range(B.N):
                idx, prev = 0, 0
                for row in range(B.N):
                    if B.B[row][col] == 0: continue
                    if prev == B.B[row][col]:
                        max_num = max(max_num, prev * 2)
                        B.B[idx - 1][col] = prev * 2
                        prev, B.B[row][col] = 0, 0
                    else:
                        prev, B.B[row][col] = B.B[row][col], 0
                        max_num = max(max_num, prev)
                        B.B[idx][col] = prev
                        idx += 1

        elif move_type == S.LEFT:
            for row in range(B.N):
                idx, prev = 0, 0
                for col in range(B.N):
                    if B.B[row][col] == 0: continue
                    if prev == B.B[row][col]:
                        max_num = max(max_num, prev * 2)
                        B.B[row][idx - 1] = prev * 2
                        prev, B.B[row][col] = 0, 0
                    else:
                        prev, B.B[row][col] = B.B[row][col], 0
                        max_num = max(max_num, prev)
                        B.B[row][idx] = prev
                        idx += 1

        elif move_type == S.DOWN:
            for col in range(B.N):
                idx, prev = B.N - 1, 0
                for row in range(B.N - 1, -1, -1):
                    if B.B[row][col] == 0: continue
                    if prev == B.B[row][col]:
                        max_num = max(max_num, prev * 2)
                        B.B[idx + 1][col] = prev * 2
                        prev, B.B[row][col] = 0, 0
                    else:
                        prev, B.B[row][col] = B.B[row][col], 0
                        max_num = max(max_num, prev)
                        B.B[idx][col] = prev
                        idx -= 1

        elif move_type == S.RIGHT:
            for row in range(B.N):
                idx, prev = B.N - 1, 0
                for col in range(B.N - 1, -1, -1):
                    if B.B[row][col] == 0: continue
                    if prev == B.B[row][col]:
                        max_num = max(max_num, prev * 2)
                        B.B[row][idx + 1] = prev * 2
                        prev, B.B[row][col] = 0, 0
                    else:
                        prev, B.B[row][col] = B.B[row][col], 0
                        max_num = max(max_num, prev)
                        B.B[row][idx] = prev
                        idx -= 1
        else:
            pass

        return max_num

    def run(self) -> None:
        if B.N == 1: print(B.B[0][0]); exit()
        self._BT(deep=1)
        print(max(B.max_check))


if __name__ == '__main__':
    P = P()
    P.run()
