"""Solution code for "BaekJoon 쇠막대기".

- Problem link: https://www.acmicpc.net/problem/10799
"""

from sys import stdin as input


class Stack:
    """ 스택 """

    def __init__(self):
        self.stack_data = []

    def append(self, data):
        self.stack_data.append(data)

    def pop(self):
        return self.stack_data.pop()

    def last_check(self):
        return self.stack_data[-1]


class P:

    def __init__(self) -> None:
        self.input_data = list(input.readline())
        self.bar_count = 0

    def result(self) -> None:
        answer = 0
        stack = Stack()
        stack.append(self.input_data[0])

        for data in self.input_data[1:]:

            if stack.last_check() == "(" and data == ")": # 레이저 찾기
                answer += self.bar_count
            elif stack.last_check() == "(" and data == "(": # 나무 증가
                answer += 1
                self.bar_count += 1
            elif stack.last_check() == ")" and data == ")": # 나무 감소
                self.bar_count -= 1

            stack.append(data)

        print(answer)


if __name__ == '__main__':
    # input = open('./10799.txt')
    P = P()
    P.result()