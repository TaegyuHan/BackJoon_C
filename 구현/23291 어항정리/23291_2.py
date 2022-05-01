"""
    Solution code for "BaekJoon 어항 정리".

    - Problem link: https://www.acmicpc.net/problem/23291
"""

from sys import stdin as input
from sys import maxsize as MAX


class S:
    """ 상태 """
    EMPTY = False


class D:
    """ 데이터 """
    COUNT: int
    END: int
    FISH_BOWLS = []
    FISH_BOWL_BOTTOM: int
    MOST_LEFT = 0

    up_row: int
    up_col: int

    @staticmethod
    def show_fish_tank():
        """ 어행 보여주기 """
        for row in D.FISH_BOWLS:
            print("\t".join(map(D._false_to_x, row)))
        print()

    @staticmethod
    def _false_to_x(x):
        """ false x로 변경 """
        if x == False:
            return "x"
        return str(x)

    @staticmethod
    def add_fish():
        """
            물고기 늘리기
            가장 작은 물고기 1마리 추가하기
        """
        tmp_max = MAX
        tmp_index = []

        for index in range(D.COUNT):
            count = D.FISH_BOWLS[D.FISH_BOWL_BOTTOM][index]
            if count < tmp_max:
                tmp_max = count
                tmp_index = [index]
            elif count == tmp_max:
                tmp_index.append(index)

        for index in tmp_index:
            D.FISH_BOWLS[D.FISH_BOWL_BOTTOM][index] += 1

    @staticmethod
    def most_left_move():
        """ 왼쪽 맨위 어항 옮기기 """
        D.FISH_BOWLS[D.FISH_BOWL_BOTTOM][D.MOST_LEFT], \
        D.FISH_BOWLS[D.FISH_BOWL_BOTTOM - 1][D.MOST_LEFT + 1] = \
            S.EMPTY, \
            D.FISH_BOWLS[D.FISH_BOWL_BOTTOM][D.MOST_LEFT]

    @staticmethod
    def _switch(go, to):
        """ 어항 변경 """
        D.FISH_BOWLS[go[0]][go[1]], D.FISH_BOWLS[to[0]][to[1]] = \
            S.EMPTY, D.FISH_BOWLS[go[0]][go[1]]

    @staticmethod
    def move_90():
        """ 90도 움직이기 """
        row = D.FISH_BOWL_BOTTOM - 1
        col = D.MOST_LEFT + 1

        while True:
            # 올리는 시작점
            up_row, up_col = row, col + 1

            # 올릴 수 있는지 확인
            fish_tank_height = D.COUNT - up_row
            up_space = D.COUNT - up_col
            if up_space < fish_tank_height: break

            # 2층 이상 어항인 곳 복사
            mrow = D.COUNT - 2
            height = 0

            for col in range(col, -1, -1):
                if not D.FISH_BOWLS[row][col]: break
                tcol = 0
                for row in range(D.COUNT - 1, row - 1, -1):
                    nrow, ncol = mrow - height, up_col + tcol

                    # 변경하기
                    D._switch((row, col), (nrow, ncol))

                    tcol += 1
                height += 1

            row, col = nrow, ncol


class P:

    def __init__(self) -> None:
        D.COUNT, D.END = map(int, input.readline().split())
        D.FISH_BOWL_BOTTOM = D.COUNT - 1
        self._init_fishbowl()

    def _init_fishbowl(self):
        """ 어항 받기 """
        for _ in range(D.COUNT - 1):
            D.FISH_BOWLS.append([S.EMPTY for _ in range(D.COUNT)])
        D.FISH_BOWLS.append(list(map(int, input.readline().split())))

    def run(self) -> None:
        D.add_fish()
        D.most_left_move()
        D.move_90()
        D.show_fish_tank()

if __name__ == '__main__':
    input = open('./23291.txt')
    P = P()
    P.run()