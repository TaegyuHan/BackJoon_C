"""
    Solution code for "BaekJoon 수도쿠"

    - Problem link: https://www.acmicpc.net/problem/2239
"""
import sys
from sys import stdin as input


class S:
    """ 상태 """
    EMPTY = 0
    SIZE = 9
    TMP_SIZE = 3


class D:
    """ 데이터 """
    BORAD = []
    EMPTY_LIST = []
    CHCEK_ROW = [set() for _ in range(S.SIZE)]
    CHCEK_COL = [set() for _ in range(S.SIZE)]
    CHCEK_POSITION = [[set() for _ in range(S.TMP_SIZE)] for _ in range(S.TMP_SIZE)]
    ANSWER = []


class P:

    def __init__(self) -> None:
        self._init_board()

    def _init_board(self):
        """ 수도쿠 데이터 받기 """
        for row in range(S.SIZE):
            tmp = list(map(int, list(input.readline().strip())))
            D.BORAD.append(tmp)
            for col in range(S.SIZE):
                if tmp[col] == S.EMPTY:
                    D.EMPTY_LIST.append((row, col))
                    continue

                D.CHCEK_ROW[row].add(tmp[col])
                D.CHCEK_COL[col].add(tmp[col])
                D.CHCEK_POSITION[row // S.TMP_SIZE][col // S.TMP_SIZE].add(tmp[col])

    def _check_num(self, current_position, num):
        """ 이미 사용한 수인지 확인 """
        row, col = current_position
        if num in D.CHCEK_ROW[row]: return False
        elif num in D.CHCEK_COL[col]: return False
        elif num in D.CHCEK_POSITION[row // S.TMP_SIZE][col // S.TMP_SIZE]: return False

        D.CHCEK_ROW[row].add(num)
        D.CHCEK_COL[col].add(num)
        D.CHCEK_POSITION[row // S.TMP_SIZE][col // S.TMP_SIZE].add(num)
        return True

    def _check_num_out(self, current_position, num):
        """ 확인 번호 빼기 """
        row, col = current_position
        D.CHCEK_ROW[row].remove(num)
        D.CHCEK_COL[col].remove(num)
        D.CHCEK_POSITION[row // S.TMP_SIZE][col // S.TMP_SIZE].remove(num)
        return

    def _show_board(self):
        """ 수도쿠 확인 확인 """
        for row in D.BORAD:
            print("".join(map(str, row)))

    def _sudoku_run(self, empty_list):
        """ 수도쿠 실행 """
        if not empty_list:
            self._show_board()
            sys.exit()
            return

        current_position, *next_empty_list = empty_list
        for num in range(1, S.SIZE + 1):
            # 넣을 수 있는지 확인
            if not self._check_num(current_position, num): continue
            row, col = current_position
            # 보드에 넣기
            D.BORAD[row][col] = num

            # 다음으로 들어가기
            self._sudoku_run(next_empty_list)

            # 보드에서 빼기
            self._check_num_out(current_position, num)
            D.BORAD[row][col] = 0

    def run(self) -> None:
        self._sudoku_run(D.EMPTY_LIST)

if __name__ == '__main__':
    # input = open('./2239.txt')
    P = P()
    P.run()


