"""
    Solution code for "BaekJoon 빈도 정렬".

    - Problem link: https://www.acmicpc.net/problem/2910
"""

from sys import stdin as input

class P:

    def __init__(self) -> None:
        self.N, self.C = map(int, input.readline().split())
        self._nums = map(int, input.readline().split())
        self.table = {}

    def run(self) -> None:
        # 데이터 받기
        for index, data in enumerate(self._nums):
            if data in self.table: self.table[data][-1] += 1
            else: self.table[data] = [index, data, 1]

        answer = []
        for data in sorted(self.table.items(), key=lambda x: (-x[1][2], x[1][0])):
            num, data = data
            _, _, count = data
            answer.extend([num]*count)
        print(*answer)


if __name__ == '__main__':
    # input = open('./2910.txt')
    P = P()
    P.run()