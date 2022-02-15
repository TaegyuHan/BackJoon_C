"""Solution code for "BaekJoon 외판원 순회2".

- Problem link: https://www.acmicpc.net/problem/10971
"""
import sys
from sys import stdin as input

class P:

    def __init__(self) -> None:
        self.N = int(input.readline())
        self.board = [list(map(int, input.readline().split()))
                      for _ in range(self.N)]

    def _backtracking(self, start: int, next: int, value: int, visited: list[int]) -> None:

        if len(visited) == self.N: # 도시를 전부 들렸을 경우
            if self.board[next][start] != 0:
                # 가장 작은 거리 계산
                self.miun_value = min(self.miun_value, value + self.board[next][start])
                return

        for i in range(self.N):
            if self.board[next][i] != 0 and \
                i not in visited and \
                value < self.miun_value:
                visited.append(i)
                self._backtracking(start, i, value + self.board[next][i], visited)
                visited.pop()

    def result(self):
        self.miun_value = sys.maxsize

        for i in range(self.N):
            self._backtracking(i, i, 0, [i])

        print(self.miun_value)


if __name__ == '__main__':
    # input = open('./10971.txt')
    P = P()
    P.result()