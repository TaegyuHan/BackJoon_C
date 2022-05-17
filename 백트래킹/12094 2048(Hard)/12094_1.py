"""
    Solution code for "BaekJoon 2048 (Hard)".

    - Problem link: https://www.acmicpc.net/problem/12094
"""

from sys import stdin as input


class S:
    ZERO = 0
    SUM_STATE = 0
    SUM = 1
    NO_SUM = 0
    NUM = 1


class B:
    """ 판 데이터 """
    N: int
    B: list[list[int]]

    @staticmethod
    def show_board():
        """ 판 보여주기 """
        for row in B.B:
            for col in row:
                print(col, end="\t")
            print()
        print()

    @staticmethod
    def left():
        """ 판을 왼쪽으로 왼쪽 이동하기 """

        for row in range(B.N):
            stack = []
            # 스택에 데이터 넣기
            for col in range(B.N):
                if not B.B[row][col]: # 0 PASS
                    continue
                elif not stack: # 처음 들어오는 수
                    stack.append((S.NO_SUM, B.B[row][col]))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[-1][S.SUM_STATE] == S.NO_SUM and \
                        stack[-1][S.NUM] == B.B[row][col]:
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, B.B[row][col]*2)) # 2배
                    continue
                stack.append((S.NO_SUM, B.B[row][col]))

            B.B[row] = [data[1] for data in stack] + [0] * (B.N - len(stack))

    @staticmethod
    def right():
        """ 판을 오른쪽으로 이동하기 """
        for row in range(B.N):
            stack = []
            # 스택에 데이터 넣기
            for col in range(B.N - 1, -1, -1):
                if not B.B[row][col]: # 0 PASS
                    continue
                elif not stack: # 처음 들어오는 수
                    stack.append((S.NO_SUM, B.B[row][col]))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[-1][S.SUM_STATE] == S.NO_SUM and \
                        stack[-1][S.NUM] == B.B[row][col]:
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, B.B[row][col]*2)) # 2배
                    continue
                stack.append((S.NO_SUM, B.B[row][col]))

            B.B[row] = [0] * (B.N - len(stack)) \
                       + [stack[i][1] for i in range(len(stack) - 1, - 1, -1)]

    @staticmethod
    def up():
        """ 판을 위로 이동하기 """
        for col in range(B.N):
            stack = []
            # 스택에 데이터 넣기
            for row in range(B.N):
                if not B.B[row][col]: # 0 PASS
                    continue
                elif not stack: # 처음 들어오는 수
                    stack.append((S.NO_SUM, B.B[row][col]))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[-1][S.SUM_STATE] == S.NO_SUM and \
                        stack[-1][S.NUM] == B.B[row][col]:
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, B.B[row][col]*2)) # 2배
                    continue
                stack.append((S.NO_SUM, B.B[row][col]))

            for row in range(B.N):
                try: B.B[row][col] = stack[row][S.NUM]
                except IndexError: B.B[row][col] = 0

    @staticmethod
    def down():
        """ 판을 아래로 이동하기 """
        for col in range(B.N):
            stack = []
            # 스택에 데이터 넣기
            for row in range(B.N - 1, -1, -1):
                if not B.B[row][col]: # 0 PASS
                    continue
                elif not stack: # 처음 들어오는 수
                    stack.append((S.NO_SUM, B.B[row][col]))
                    continue

                # 맨위의 수가 더해진 수가 아니면서 같은 경우
                if stack[-1][S.SUM_STATE] == S.NO_SUM and \
                        stack[-1][S.NUM] == B.B[row][col]:
                    stack.pop() # 스택 빼기
                    stack.append((S.SUM, B.B[row][col]*2)) # 2배
                    continue
                stack.append((S.NO_SUM, B.B[row][col]))

            for row in range(B.N - 1, -1, -1):
                try: B.B[row][col] = stack[B.N - 1 - row][S.NUM]
                except IndexError: B.B[row][col] = 0


class P:

    def __init__(self) -> None:
        self._input_data()

    def _input_data(self):
        """ 데이터 받기 """
        B.N = int(input.readline())
        B.B = [list(map(int, input.readline().strip().split())) for _ in range(B.N)]

    def run(self) -> None:
        """ 실행 """


if __name__ == '__main__':
    input = open('./12094.txt')
    P = P()
    P.run()