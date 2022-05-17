"""
    Solution code for "BaekJoon 2048 (Hard)".

    - Problem link: https://www.acmicpc.net/problem/12094
"""

from sys import stdin as input
input = open('./12100.txt')


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

    def left(self):
        """ 왼쪽으로 이동 """
        next_board = []
        max_value = 0

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
                    sum_value = current_value * 2
                    stack.pop()  # 스택 빼기
                    stack.append((S.SUM, sum_value))  # 2배

                    if sum_value > max_value: max_value = sum_value # max 최신화
                    continue

                stack.append((S.NO_SUM, current_value))
            next_board.append([data[S.NUM] for data in stack]
                              + [0] * (self.N - len(stack)))
        return max_value, next_board

    def right(self):
        """ 오른쪽으로 이동 """
        next_board = []
        max_value = 0

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
                    sum_value = current_value * 2
                    stack.pop()  # 스택 빼기
                    stack.append((S.SUM, sum_value))  # 2배

                    if sum_value > max_value: max_value = sum_value  # max 최신화

                    continue
                stack.append((S.NO_SUM, current_value))
            next_board.append([0] * (self.N - len(stack))
                              + [stack[i][S.NUM] for i in range(len(stack) - 1, - 1, -1)])

        return max_value, next_board

    def up(self):
        """ 판을 위로 이동하기 """
        next_board = [[] for _ in range(self.N)]
        max_value = 0

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
                    sum_value = current_value * 2
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, sum_value)) # 2배

                    if sum_value > max_value: max_value = sum_value  # max 최신화
                    continue

                stack.append((S.NO_SUM, current_value))

            # 복사하기
            for row in range(self.N):
                try: next_board[row][col] = stack[row][S.NUM]
                except IndexError: next_board[row][col] = 0

        return max_value, next_board

    def down(self):
        """ 판을 아래로 이동하기 """
        next_board = [[] for _ in range(self.N)]
        max_value = 0

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
                    sum_value = current_value * 2
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, sum_value)) # 2배

                    if sum_value > max_value: max_value = sum_value  # max 최신화
                    continue

                stack.append((S.NO_SUM, current_value))

            for row in range(self.N - 1, -1, -1):
                try: next_board[row][col] = stack[self.N - 1 - row][S.NUM]
                except IndexError: next_board[row][col] = 0

        return max_value, next_board


class P:

    def _backtracking(self, board: Board, deep: int):
        """ 백트래킹 """
        if deep == 5:
            return

        for i, (max_value, nboard) in enumerate([board.left(), board.right() ,board.up(), board.down()]):
            if max_value > self._max_vaule: self._max_vaule = max_value # max 최신화

            self._backtracking(Board(nboard), deep + 1)

    def run(self) -> None:
        self._max_vaule = 0
        B = Board([list(map(int, input.readline().split())) for _ in range(Board.N)])
        self._backtracking(B, deep=0)
        print(self._max_vaule)

        # B.show_board(B.left())
        # B.show_board(B.right())
        # B.show_board(B.up())
        # B.show_board(B.down())

if __name__ == '__main__':
    P = P()
    P.run()