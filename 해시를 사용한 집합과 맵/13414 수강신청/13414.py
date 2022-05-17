"""
    Solution code for "BaekJoon 수강신청".

    - Problem link: https://www.acmicpc.net/problem/13414
"""

from sys import stdin as input

class D:
    """ 데이터 """
    CUT: int
    COUNT: int


class P:

    def __init__(self) -> None:
        D.CUT, D.COUNT = map(int, input.readline().split())

    def run(self) -> None:
        wait = {}
        for time in range(D.COUNT):
            key = input.readline().strip()
            # 없으면 생성
            wait[key] = time

        for school_number, _ in sorted(wait.items(), key=lambda x:x[1])[:D.CUT]:
            print(school_number)


if __name__ == '__main__':
    # input = open('./13414.txt')
    P = P()
    P.run()