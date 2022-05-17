"""
    Solution code for "BaekJoon 아기 상어".

    - Problem link: https://www.acmicpc.net/problem/16236

    구현 요구사항

    상어
        - 가장 처음에 아기 상어의 크기는 2
        - 1초에 상하좌우로 인접한 한 칸씩 이동한다.

        - 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.

        - 나머지 칸은 모두 지나갈 수 있다.
            - 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
            - 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

        - 어디로 이동할지 결정하는 방법은 아래와 같다.
            1. 더이상 먹을 물고기가 없으면 멈춤
            2. 1마리 발견시 그걸 먹으러감
            4. 2마리 이상이면
                - 가장 가까운 물고기 먹음
                - 거리 같은게 2마리 이상이면
                    - 가장 왼쪽, 위
"""
from sys import stdin as input
from collections import deque
from copy import copy


class S:
    """ 상어 """
    SHARK = 9
    EMPTY = 0


class M:
    """ 상어 움직임 """
    LEN = 4
    X = [-1, 0, 0, 1]
    Y = [0, -1, 1, 0]


class FP:
    """ 어항 """
    N: int
    SEA = []
    ANSWER = 0
    eat_fish_list = []

    s_size = 2
    s_eat_count = 2
    s_row = 0
    s_col = 0

    @staticmethod
    def show_sea():
        """ 바다 확인하기 """
        for row in FP.SEA:
            print(*row)

    @staticmethod
    def shark_position():
        """ 상어 위치 """
        return FP.s_row, FP.s_col

    @staticmethod
    def shark_move(row, col):
        """ 상어 이동 """
        FP.SEA[FP.s_row][FP.s_col] = S.EMPTY
        FP.SEA[row][col] = S.SHARK
        FP.s_row, FP.s_col = row, col


class P:

    def __init__(self) -> None:
        self._input_data()
        self._answer = 0

    def _input_data(self):
        """ 데이터 받기 """
        FP.N = int(input.readline())
        for row in range(FP.N):
            tmp = list(map(int, input.readline().strip().split()))
            FP.SEA.append(tmp)
            for col in range(FP.N):
                if tmp[col] != S.SHARK: continue
                FP.s_row, FP.s_col = row, col
                FP.SEA[FP.s_row][FP.s_col] = S.EMPTY

    def _bfs(self):
        """ 우선 넓이 탐색 """
        visited = [[False for _ in range(FP.N)] for _ in range(FP.N)]
        q = deque([(FP.s_row, FP.s_col, 0)])
        catch_fish = []

        while q:
            crow, ccol, move_count = q.popleft()

            # 상어 잡아 먹음
            if FP.SEA[crow][ccol] < FP.s_size \
                    and FP.SEA[crow][ccol] != S.EMPTY:
                catch_fish.append((crow, ccol, move_count))

            # 이미 방문한 곳
            if visited[crow][ccol]: continue
            visited[crow][ccol] = True

            for i in range(M.LEN):
                nrow, ncol = crow + M.X[i], ccol + M.Y[i]
                if not (0 <= nrow < FP.N and 0 <= ncol < FP.N): continue
                if visited[nrow][ncol]: continue  # 이미 방문
                if FP.SEA[nrow][ncol] > FP.s_size: continue  # 자신 보다 큰 물고기
                q.append((nrow, ncol, move_count + 1))

        # 잡을 수 있는 상어가 있는 경우
        if catch_fish:
            catch_fish.sort(key=lambda x: (x[2], x[0], x[1]))
            nrow, ncol, count = catch_fish[0]
            FP.SEA[nrow][ncol] = S.EMPTY
            FP.ANSWER += count
            FP.s_row, FP.s_col = nrow, ncol

            # 상어 먹는 수치 감소
            FP.s_eat_count -= 1
            if FP.s_eat_count <= 0:
                FP.s_size += 1
                FP.s_eat_count = copy(FP.s_size)
            return True
        return False

    def run(self) -> None:
        while self._bfs():
            pass
        print(FP.ANSWER)


if __name__ == '__main__':
    # input = open('./16236.txt')
    P = P()
    P.run()
