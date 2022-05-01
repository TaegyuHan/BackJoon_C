"""
    Solution code for "BaekJoon 창고 다각형".

    - Problem link: https://www.acmicpc.net/problem/
"""

from sys import stdin as input


class Stack:
    """ 스택 """
    data_count: int
    sort_data = []
    data = []

    @staticmethod
    def show_data():
        """ 스택 보여주기 """
        print(Stack.data)


class P:

    def _input_data(self):
        """ 데이터 받기 """
        Stack.data_count = int(input.readline())
        Stack.sort_data = sorted([tuple(map(int, input.readline().split()))
                                  for _ in range(Stack.data_count)], key=lambda x:x[0])

    def run(self) -> None:
        self._input_data()

        answer = 0

        left_list = []
        right_list = []
        left_tmp = 0
        right_tmp = 0
        revers_index = Stack.data_count - 1
        for left in range(Stack.data_count):
            right = revers_index - left
            if left_tmp <= (left_y := Stack.sort_data[left][1]):
                left_list.append(Stack.sort_data[left])
                left_tmp = left_y

            if right_tmp <= Stack.sort_data[right][1]:
                right_list.append(Stack.sort_data[right])
                right_tmp = Stack.sort_data[right][1]

        bar_list = sorted(list(set(left_list + right_list)), key=lambda x:x[0])

        # 넓이
        for index in range(len(bar_list) - 1):
            (x1, y1), (x2, y2) = bar_list[index], bar_list[index + 1]
            width = abs(x2 - x1)
            if y1 <= y2: height = y1
            elif y1 > y2: height = y2
            answer += width*height

        print(answer + right_tmp)

if __name__ == '__main__':
    # input = open('./2304.txt')
    P = P()
    P.run()