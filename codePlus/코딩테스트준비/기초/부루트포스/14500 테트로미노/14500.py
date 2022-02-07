# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.ROW, self.COL = map(int, input.readline().split())
        self.BOARD = [list(map(int, input.readline().split()))
                      for _ in range(self.ROW)]
        self.box_count = 4

    def _shape1(self, row: int, col: int) -> int:
        """
            ㅁㅁㅁㅁ 모양 확인

        :param row: row 시작
        :param col: col 시작
        :return: 사각형이 정확히 하나의 칸을 포함하는 값 출력
        """

        type_1, type_2 = 0, 0
        if (end_col := col + 4) <= self.COL:
            type_1 = sum(map(lambda x: self.BOARD[row][x],
                             range(col, end_col)))

        if (end_row := row + 4) <= self.ROW:
            type_2 = sum(map(lambda x: self.BOARD[x][col],
                             range(row, end_row)))

        return max(type_1, type_2)

    def _shape2(self, row: int, col: int) -> int:
        """
            ㅁ
            ㅁ
            ㅁㅁ

               ㅁ
            ㅁ ㅁ ㅁ

               ㅁ ㅁ
            ㅁ ㅁ

            모양 확인

        :param row: row 시작
        :param col: col 시작
        :return: 사각형이 정확히 하나의 칸을 포함하는 값
        """

        shape1_sum = [0 for _ in range(8)]
        shape2_sum = [0 for _ in range(8)]
        shape1 = [
            (
                (0, 0),  #
                (1, 0),  # #
                (1, 1),    #
                (2, 1)
            ),
            (
                (0, 1),    #
                (1, 0),  # #
                (1, 1),  #
                (2, 0)
            ),
            (
                (0, 0),  #
                (1, 0),  #
                (2, 0),  # #
                (2, 1)
            ),
            (
                (0, 1),    #
                (1, 1),    #
                (2, 1),  # #
                (2, 0)
            ),
            (
                (0, 0),  # #
                (0, 1),    #
                (1, 1),    #
                (2, 1)
            ),
            (
                (0, 0),  # #
                (0, 1),  #
                (1, 0),  #
                (2, 0)
            ),
            (
                (0, 0),  #
                (1, 0),  # #
                (1, 1),  #
                (2, 0)
            ),
            (
                (0, 1),    #
                (1, 0),  # #
                (1, 1),    #
                (2, 1)
            )
        ]

        shape2 = [
            (
                (1, 0),    # #
                (0, 1),  # #
                (1, 1),
                (0, 2)
            ),
            (
                (0, 0),  # #
                (0, 1),    # #
                (1, 1),
                (1, 2)
            ),
            (
                (0, 0),  # # #
                (1, 0),  #
                (0, 1),
                (0, 2)
            ),
            (
                (0, 2),      #
                (1, 0),  # # #
                (1, 1),
                (1, 2)
            ),
            (
                (0, 0),  # # #
                (0, 1),      #
                (0, 2),
                (1, 2)
            ),
            (
                (0, 0),  #
                (1, 0),  # # #
                (1, 1),
                (1, 2)
            ),
            (
                (1, 0),  # #
                (1, 1),    # #
                (0, 1),
                (1, 2)
            ),
            (
                (0, 0),  # # #
                (0, 1),    #
                (0, 2),
                (1, 1)
            )
        ]

        if row + 2 < self.ROW and col + 1 < self.COL:
            for i, shape in enumerate(shape1):
                for row_plus, col_plus  in shape:
                    shape1_sum[i] += self.BOARD[row + row_plus][col + col_plus]

        if row + 1 < self.ROW and col + 2 < self.COL:
            for i, shape in enumerate(shape2):
                for row_plus, col_plus in shape:
                    shape2_sum[i] += self.BOARD[row + row_plus][col + col_plus]

        return max(max(shape1_sum),max(shape2_sum))

    def _shape3(self, row: int, col: int) -> int:

        shape_sum = 0
        shape = [
            (
                (0, 0),  # #
                (0, 1),  # #
                (1, 1),
                (1, 0)
            ),
        ]

        if row + 1 < self.ROW and col + 1 < self.COL:
            for shape in shape:
                for row_plus, col_plus  in shape:
                    shape_sum += self.BOARD[row + row_plus][col + col_plus]

        return shape_sum

    def result(self) -> None:
        answer = []
        for row in range(self.ROW):
            for col in range(self.COL):
                answer.append(max(
                    self._shape1(row, col),
                    self._shape2(row, col),
                    self._shape3(row, col)
                ))

        print(max(answer))


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./14500.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)

