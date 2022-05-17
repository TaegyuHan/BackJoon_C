"""
    Solution code for "BaekJoon 앵무새".

    - Problem link: https://www.acmicpc.net/problem/14713
"""

from sys import stdin as input
from collections import deque

class P:

    def run(self) -> None:
        count = int(input.readline())
        datas = [deque(input.readline().strip().split()) for _ in range(count)]
        result = deque(input.readline().strip().split())

        while result:
            not_find = True
            word = result.popleft()
            for i in range(len(datas)):
                if not datas[i]: continue
                if word == datas[i][0]:
                    datas[i].popleft()
                    not_find = False
                    break

            if not_find:
                print("Impossible")
                return
        print("Possible")


if __name__ == '__main__':
    input = open('./14713.txt')
    P = P()
    P.run()