"""
    Solution code for "BaekJoon 스타트링크".

    - Problem link: https://www.acmicpc.net/problem/5014
"""
from sys import stdin as input
from collections import deque


class M:
    """ 엘레베이터 움직임 """
    ALL = []


class B:
    """ 빌딩 """
    MAX: int
    START: int
    END: int
    UP: int
    DOWN: int
    VISTED = []


class P:

    def __init__(self) -> None:
        B.MAX, B.START, B.END, B.UP, B.DOWN = map(int, input.readline().split())
        M.ALL = [B.UP, -B.DOWN]

    def _bfs(self):
        """ 우선 넓이 탐색 """
        q = deque([B.START])
        B.VISTED = [0 for _ in range(B.MAX + 1)]
        B.VISTED[B.START] = 1
        while q:
            current_position = q.popleft()
            if current_position == B.END:
                return B.VISTED[current_position] - 1

            for move in M.ALL:
                next_position = current_position + move
                if not (1 <= next_position <= B.MAX): continue
                if B.VISTED[next_position]: continue
                B.VISTED[next_position] = B.VISTED[current_position] + 1
                q.append(next_position)

        return "use the stairs"

    def run(self) -> None:
        print(self._bfs())


if __name__ == '__main__':
    # input = open('./5014.txt')
    P = P()
    P.run()