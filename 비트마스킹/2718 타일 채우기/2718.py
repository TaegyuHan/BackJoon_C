"""
    Solution code for "BaekJoon 타일 채우기".

    - Problem link: https://www.acmicpc.net/problem/2718
"""

from sys import stdin as input


class D:
    """ 데이터 """
    TEST_CASE: int
    DP = [0, 1, 5]


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _dp(self):
        """ 다이나믹 프로그래밍 """
        for i in range(3, int(input.readline()) + 1):
            D.DP.append(D.DP[i - 2] * D.DP[i - 1])

    def run(self) -> None:
        for _ in range(D.TEST_CASE):
            self._dp()
        print(D.DP[7])

if __name__ == '__main__':
    input = open('./2718.txt')
    P = P()
    P.run()