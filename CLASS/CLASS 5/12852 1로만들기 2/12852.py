"""
    Solution code for "BaekJoon 1로 만들기 2".

    - Problem link: https://www.acmicpc.net/problem/12852
"""

from sys import stdin as input


class S:
    """ 타입 """
    ONE = 1
    TWO = 2
    THREE = 3


class D:
    """ 숫자 """
    NUMBER: int
    DP = [0, 0, 1, 1]
    DP_HISTORY = [[], [1], [1, 2], [1, 3]]


class P:

    def __init__(self) -> None:
        D.NUMBER = int(input.readline())

    def run(self) -> None:
        """ 실행 """
        if D.NUMBER <= 3:
            print(D.DP[D.NUMBER])
            print(*D.DP_HISTORY[D.NUMBER][::-1])
            return

        for i in range(4, D.NUMBER + 1):

            # 1더하기
            next_num = D.DP[i - 1] + 1
            type = S.ONE

            if i % 3 == 0: # 3으로 나눠지는 경우
                if next_num > D.DP[i // 3] + 1:
                    type = S.THREE
                    next_num = D.DP[i // 3] + 1
            if i % 2 == 0:  # 2으로 나눠지는 경우
                if next_num > D.DP[i // 2] + 1:
                    type = S.TWO
                    next_num = D.DP[i // 2] + 1

            if type == S.ONE:
                next_history = D.DP_HISTORY[i - 1].copy()
            elif type == S.TWO:
                next_history = D.DP_HISTORY[i // 2].copy()
            elif type == S.THREE:
                next_history = D.DP_HISTORY[i // 3].copy()
            next_history.append(i)

            D.DP.append(next_num)
            D.DP_HISTORY.append(next_history)

        print(D.DP[D.NUMBER])
        print(*D.DP_HISTORY[D.NUMBER][::-1])


if __name__ == '__main__':
    # input = open('./12852.txt')
    P = P()
    P.run()