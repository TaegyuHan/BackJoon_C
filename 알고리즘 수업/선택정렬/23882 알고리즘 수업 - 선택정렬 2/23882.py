"""
    Solution code for "BaekJoon 알고리즘 수업 - 선택정렬 2".

    - Problem link: https://www.acmicpc.net/problem/23882
"""
from sys import stdin as input


class P:

    def __init__(self) -> None:
        self._num, self._check_number = map(int, input.readline().split())
        self._list = list(map(int, input.readline().split()))

    def selection_sort(self):
        """ 선택 정렬 """
        count = 0
        for i in range(self._num - 1, -1, -1):
            index_max = i
            for j in range(i - 1, -1, -1):
                if self._list[index_max] < self._list[j]:
                    index_max = j

            # 변경 횟수 추가
            if i != index_max:
                count += 1

            # 변경
            self._list[i], self._list[index_max] =\
                self._list[index_max], self._list[i]

            # 결과 출력
            if count == self._check_number:
                print(*self._list)
                return

        print(-1)

    def run(self) -> None:
        self.selection_sort()


if __name__ == '__main__':
    # input = open('./23882.txt')
    P = P()
    P.run()