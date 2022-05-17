"""
    Solution code for "BaekJoon 2048 (Hard)".

    - Problem link: https://www.acmicpc.net/problem/12094
"""

from sys import stdin as input
input = open('./12094.txt')

class S:
    ZERO = 0
    SUM_STATE = 0
    SUM = 1
    NO_SUM = 0
    NUM = 1
    TOP = -1


class Board:
    """ 판 """
    N = int(input.readline())
    MAX = 10

    def __init__(self, board):
        self._board = board

    @staticmethod
    def show_board(board):
        """ 판 보여주기 """
        for row in board:
            print(*row)

    @property
    def board(self):
        """ 판 수정하기 """
        return self._board

    def max(self):
        """ 현재 최대값 반환 """
        return max([max(row) for row in self._board])

    def _change_check(self, board):
        """ 변화 확인 """
        if board == self._board: return True
        return False

    def left(self):
        """ 왼쪽으로 이동 """
        next_board = []
        max_value = 0
        change_check = True

        for row in range(self.N):
            stack = []
            for col in range(self.N):
                current_value = self._board[row][col]
                if current_value > max_value: max_value = current_value # max 최신화

                if not current_value: continue # 0 PASS
                elif not stack:  # 처음 들어오는 수
                    stack.append((S.NO_SUM, current_value))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[S.TOP][S.SUM_STATE] == S.NO_SUM and \
                        stack[S.TOP][S.NUM] == current_value:
                    change_check = False
                    sum_value = current_value * 2
                    stack.pop()  # 스택 빼기
                    stack.append((S.SUM, sum_value))  # 2배

                    if sum_value > max_value: max_value = sum_value # max 최신화
                    continue

                stack.append((S.NO_SUM, current_value))

            tmp = []
            for i in range(len(stack)):
                tmp.append(stack[i][S.NUM])
                if change_check and self._board[row][i] != tmp[i]:
                    change_check = False

            for i in range(self.N - len(stack)):
                tmp.append(0)
                if change_check and self._board[row][i] != tmp[i]:
                    change_check = False

            next_board.append(tmp)

        return max_value, next_board, change_check

    def right(self):
        """ 오른쪽으로 이동 """
        next_board = []
        max_value = 0
        change_check = True

        for row in range(self.N):
            stack = []
            for col in range(self.N - 1, -1, -1):
                current_value = self._board[row][col]
                if current_value > max_value: max_value = current_value  # max 최신화

                if not current_value: continue # 0 PASS
                elif not stack:  # 처음 들어오는 수
                    stack.append((S.NO_SUM, current_value))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[S.TOP][S.SUM_STATE] == S.NO_SUM and \
                        stack[S.TOP][S.NUM] == current_value:
                    change_check = True
                    sum_value = current_value * 2
                    stack.pop()  # 스택 빼기
                    stack.append((S.SUM, sum_value))  # 2배

                    if sum_value > max_value: max_value = sum_value  # max 최신화

                    continue
                stack.append((S.NO_SUM, current_value))

            tmp = []
            for i in range(self.N - len(stack)):
                tmp.append(0)
                if change_check and self._board[row][i] != tmp[i]:
                    change_check = False

            for i in range(len(stack) - 1, - 1, -1):
                tmp.append(stack[i][S.NUM])
                if change_check and self._board[row][i] != tmp[i]:
                    change_check = False

            next_board.append(tmp)

        return max_value, next_board, change_check

    def up(self):
        """ 판을 위로 이동하기 """
        next_board = [[] for _ in range(self.N)]
        max_value = 0
        change_check = True

        for col in range(self.N):
            stack = []
            # 스택에 데이터 넣기
            for row in range(self.N):
                current_value = self._board[row][col]
                next_board[row].append(0)
                if current_value > max_value: max_value = current_value  # max 최신화

                if not current_value: continue# 0 PASS
                elif not stack: # 처음 들어오는 수
                    stack.append((S.NO_SUM, current_value))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[S.TOP][S.SUM_STATE] == S.NO_SUM and \
                        stack[S.TOP][S.NUM] == current_value:
                    change_check = False
                    sum_value = current_value * 2
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, sum_value)) # 2배

                    if sum_value > max_value: max_value = sum_value  # max 최신화
                    continue

                stack.append((S.NO_SUM, current_value))

            # 복사하기
            for row in range(self.N):
                try:
                    next_board[row][col] = stack[row][S.NUM]
                    if change_check and self._board[row][col] != next_board[row][col]:
                        change_check = False

                except IndexError:
                    next_board[row][col] = 0
                    if change_check and self._board[row][col] != next_board[row][col]:
                        change_check = False

        return max_value, next_board, change_check

    def down(self):
        """ 판을 아래로 이동하기 """
        next_board = [[] for _ in range(self.N)]
        max_value = 0
        change_check = False

        for col in range(self.N):
            stack = []
            # 스택에 데이터 넣기
            for row in range(self.N - 1, -1, -1):
                current_value = self._board[row][col]
                next_board[row].append(0)
                if current_value > max_value: max_value = current_value  # max 최신화

                if not current_value: continue # 0 PASS

                elif not stack: # 처음 들어오는 수
                    stack.append((S.NO_SUM, current_value))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[S.TOP][S.SUM_STATE] == S.NO_SUM and \
                        stack[S.TOP][S.NUM] == current_value:
                    change_check = False
                    sum_value = current_value * 2
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, sum_value)) # 2배

                    if sum_value > max_value: max_value = sum_value  # max 최신화
                    continue

                stack.append((S.NO_SUM, current_value))

            for row in range(self.N - 1, -1, -1):
                try:
                    next_board[row][col] = stack[self.N - 1 - row][S.NUM]
                    if change_check and self._board[row][col] != next_board[row][col]:
                        change_check = False

                except IndexError:
                    next_board[row][col] = 0
                    if change_check and self._board[row][col] != next_board[row][col]:
                        change_check = False

        return max_value, next_board, change_check


class P:

    def _backtracking(self, board: Board, deep: int):
        """ 백트래킹 """

        if deep == board.MAX:
            return

        for max_value, nboard, change_ceck in [board.left(), board.right(), board.up(), board.down()]:
            if change_ceck: continue
            print(deep, max_value, self._max_vaule)
            tmax, tdeep = self._max_vaule
            if max_value > tmax: self._max_vaule = (max_value, deep) # max 최신화
            if max_value == tmax and deep < tdeep: self._max_vaule = (max_value, deep) # max 최신화
            tmax, tdeep = self._max_vaule
            diff = tdeep - deep

            if diff < 0 and max_value < tdeep: continue
            if diff > 0 and max_value <= tdeep*(0.5**diff): continue


            self._backtracking(Board(nboard), deep + 1)

    def run(self) -> None:

        B = Board([list(map(int, input.readline().split())) for _ in range(Board.N)])
        self._max_vaule = B.max(), 0
        # print(self._max_vaule)
        self._backtracking(B, deep=0)
        print(self._max_vaule[0])

        # B.show_board(B.left())
        # B.show_board(B.right())
        # B.show_board(B.up())
        # B.show_board(B.down())

if __name__ == '__main__':
    P = P()
    P.run()