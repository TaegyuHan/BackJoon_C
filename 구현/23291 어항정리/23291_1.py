"""
    Solution code for "BaekJoon 어항 정리".

    - Problem link: https://www.acmicpc.net/problem/23291
"""

from sys import stdin as input
from sys import maxsize as MAX
from collections import deque
from copy import deepcopy


class S:
    """ 상태 """
    ONE = 0
    EMPTY_FISH_TANK = False
    BOTTOM = -1
    MOST_LFET = 0
    VISITED = True
    NO_VISITED = False
    FOLD_COUNT = 2


class M:
    """ 이동하기 """
    ALL = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]


class D:
    """ 데이터 """
    fish_tank_count: int
    break_number: int
    fish_tank = []


class P:

    def __init__(self) -> None:
        D.fish_tank_count, D.break_number = map(int, input.readline().split())
        self._init_fish_tank()

    def _false_to_x(self, x):
        """ false x로 변경 """
        if x == False:
            return "x"
        return str(x)

    def _show_fish_tank(self):
        """ 어행 보여주기 """
        for row in D.fish_tank:
            print("\t".join(map(self._false_to_x, row)))
        print()

    def _init_fish_tank(self):
        """ 어항 생성 """
        for _ in range(D.fish_tank_count - 1):
            D.fish_tank.append([S.EMPTY_FISH_TANK for _ in range(D.fish_tank_count)])
        D.fish_tank.append(list(map(int, input.readline().split())))

    def _add_fish(self):
        """
            물고기 늘리기
            가장 작은 물고기 1마리 추가하기
        """
        tmp_max = MAX
        tmp_index = []

        for index in range(D.fish_tank_count):
            count = D.fish_tank[S.BOTTOM][index]
            if count < tmp_max:
                tmp_max = count
                tmp_index = [index]
            elif count == tmp_max:
                tmp_index.append(index)

        for index in tmp_index:
            D.fish_tank[S.BOTTOM][index] += 1

    def _raise_left_fish_tank(self):
        """ 왼쪽 어항 올리기 """
        D.fish_tank[S.BOTTOM][S.MOST_LFET], D.fish_tank[S.BOTTOM - 1][S.MOST_LFET + 1] = \
            S.EMPTY_FISH_TANK, D.fish_tank[S.BOTTOM][S.MOST_LFET]

    def _90_degree_turn(self):
        """
            어항 90도 회전해서 올리기

            1층의 수 보다는 적을 떄 까지 적용
        """
        row, col = D.fish_tank_count - 2, 1
        while True:

            # 올리는 시작점
            up_row, up_col = row, col + 1

            # 올릴 수 있는지 확인
            fish_tank_height = D.fish_tank_count - up_row
            up_space = D.fish_tank_count - up_col
            if up_space < fish_tank_height: break

            # 2층 이상 어항인 곳 복사
            mrow = D.fish_tank_count - 2
            height = 0

            for col in range(col, -1, -1):
                if not D.fish_tank[row][col]: break
                tcol = 0
                for row in range(D.fish_tank_count - 1, row - 1, -1):
                    nrow, ncol = mrow - height, up_col + tcol

                    # 변경하기
                    self._switch((row, col), (nrow, ncol))

                    tcol += 1
                height += 1

            row, col = nrow, ncol

    def _switch(self, go, to):
        """ 어항 변경 """
        D.fish_tank[go[0]][go[1]], D.fish_tank[to[0]][to[1]] = \
            S.EMPTY_FISH_TANK, D.fish_tank[go[0]][go[1]]

    def _fish_comparison(self):
        """
            물고기 비교 하기

            어항 2개를 비교 후 차이에 5를 나누 값을 더 적은 쪽은 더하고 큰쪽은 뺌
        """
        end_position = D.fish_tank_count - 1
        visited = set()
        tmp_fish_tank = deepcopy(D.fish_tank)
        q = deque([(end_position, end_position)])

        while q:
            crow, ccol = q.popleft()
            # 이미 확인한 부분
            if (position := f"{crow},{ccol}") in visited: continue
            visited.add(position)

            for go in M.ALL:
                trow, tcol = go
                nrow, ncol = crow + trow, ccol + tcol

                # 범위가 아니면 PASS
                if not (0 <= nrow < D.fish_tank_count
                        and 0 <= ncol < D.fish_tank_count): continue

                # 어항이 아니면 PASS
                if not D.fish_tank[nrow][ncol]: continue

                # 이미 확인한 부분
                if f"{nrow},{ncol}" in visited: continue

                ccount, ncount = \
                    D.fish_tank[crow][ccol], D.fish_tank[nrow][ncol]

                # 둘 계산
                tmp = abs(ccount - ncount)
                diff = tmp // 5
                if ccount - ncount > 0:
                    tmp_fish_tank[crow][ccol] -= diff
                    tmp_fish_tank[nrow][ncol] += diff

                elif ccount - ncount < 0:
                    tmp_fish_tank[crow][ccol] += diff
                    tmp_fish_tank[nrow][ncol] -= diff

                q.append((nrow, ncol))

        # 계산 결과 저장
        D.fish_tank = tmp_fish_tank

    def _spread_fish_tank(self):
        """ 어항 펼치기 """
        spread_end_col = S.MOST_LFET

        # 오른쪽 에서부터 2층 첫번쨰 찾기
        col_list = []
        for col in range(D.fish_tank_count - 1, -1, -1):
            if D.fish_tank[S.BOTTOM - 1][col]:
                col_list.append(col)

        # 높이 알기
        for row in range(D.fish_tank_count):
            if D.fish_tank[row][col_list[S.ONE]]: break

        # 펼치기
        for i in range(len(col_list) - 1, -1, -1):
            for hrow in range(D.fish_tank_count - 1, row - 1, -1):

                # 어항 옮기기
                # 어항 이동
                self._switch((hrow, col_list[i]), (S.BOTTOM, spread_end_col))

                spread_end_col += 1

    def _180_degree_turn(self):
        """ 어항 180도 접기 """
        # 180도 뒤집기 1번 째
        start_col = D.fish_tank_count // 2
        mcol = D.fish_tank_count // 2
        for col in range(start_col - 1, - 1, -1):

            # # 어항 이동
            D.fish_tank[S.BOTTOM][col], D.fish_tank[S.BOTTOM - 1][mcol] = \
                S.EMPTY_FISH_TANK, D.fish_tank[S.BOTTOM][col]

            mcol += 1

        # 180도 뒤집기 2번 째
        end_col = start_col
        start_col = D.fish_tank_count - start_col // 2
        up_row = 1
        for row in range(0, 2):
            mcol = start_col
            for col in range(start_col - 1, end_col - 1, -1):

                # 어항 이동
                D.fish_tank[S.BOTTOM - up_row][col], D.fish_tank[S.BOTTOM - 2 - row][mcol] = \
                    S.EMPTY_FISH_TANK, D.fish_tank[S.BOTTOM - up_row][col]

                mcol += 1
            up_row -= 1

    def _max_min_diff(self):
        """ 최대 최서 차이 """
        if max(D.fish_tank[S.BOTTOM]) \
                - min(D.fish_tank[S.BOTTOM]) <= D.break_number:
            return True
        return False

    def run(self) -> None:
        answer_count = 0
        while True:

            if self._max_min_diff():
                # self._show_fish_tank()
                print(answer_count)
                return

            self._add_fish()
            self._raise_left_fish_tank()

            self._90_degree_turn()
            self._fish_comparison()
            self._spread_fish_tank()

            self._180_degree_turn()
            self._fish_comparison()
            self._spread_fish_tank()

            answer_count += 1

if __name__ == '__main__':
    # input = open('./23291.txt')
    P = P()
    P.run()
