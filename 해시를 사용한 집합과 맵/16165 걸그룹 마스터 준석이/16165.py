"""
    Solution code for "BaekJoon 걸그룹 마스터 준석이".

    - Problem link: https://www.acmicpc.net/problem/16165
"""

from sys import stdin as input


class P:

    def __init__(self):
        self._list_table = []
        self._dict_table = {}

    def _input_group_data(self, i):
        """ 그룹 데이터 받기 """
        group_name = input.readline().strip()
        member_num = int(input.readline())

        self._list_table.append(group_name)
        self._dict_table[group_name] = []
        for _ in range(member_num):
            name = input.readline().strip()
            self._dict_table[name] = i
            self._dict_table[group_name].append(name)

    def _tset(self):
        """ 테스트 진행하기 """
        data = input.readline().strip()
        cmd_type = int(input.readline())

        if cmd_type == 1:
            print(self._list_table[self._dict_table[data]])
        elif cmd_type == 0:
            for name in sorted(self._dict_table[data]):
                print(name)

    def run(self) -> None:
        group, test = map(int, input.readline().split())
        for i in range(group):
            self._input_group_data(i)

        for _ in range(test):
            self._tset()


if __name__ == '__main__':
    # input = open('./16165.txt')
    P = P()
    P.run()