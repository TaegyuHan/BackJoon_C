"""
    Solution code for "BaekJoon N-Queen".

    - Problem link: https://www.acmicpc.net/problem/9663
"""
from sys import stdin as input


class D:
    """ Data """
    N: int
    board = []
    visited = []


class P:

    def __init__(self) -> None:
        D.N = int(input.readline())
        D.board = [0 for _ in range(D.N)]

    def _check(self, n):
        """ 확인하기 """
        for i in range(n):
            if abs(D.board[n] - D.board[i]) == abs(n - i) \
                    or (D.board[n] == D.board[i]):
                return False
        return True

    def _queen(self, depth):
        """ 퀸 들어가기 """
        if depth == D.N:
            self.answer += 1
            return

        for i in range(D.N):
            D.board[depth] = i
            if self._check(depth):
                self._queen(depth + 1)

    def run(self) -> None:
        self.answer = 0
        self._queen(0)
        print(self.answer)


if __name__ == '__main__':
    input = open('./9663.txt')
    P = P()
    P.run()