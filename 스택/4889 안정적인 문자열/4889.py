"""
    Solution code for "BaekJoon 안정적인 문자열".

    - Problem link: https://www.acmicpc.net/problem/4889
"""

from sys import stdin as input

class Stack:
    """ 스택 """
    pair = {
        "{": "}",
        "}": "{"
    }

    def __init__(self, data):
        self.data = data
        self.stack = []
        self.count = 0

    def input_stack(self):
        """ 최소 연산 수 """
        for data in self.data:
            # 스택이 비었을때
            if self._stack_empty():
                self.stack.append(data)
                continue

            top = self._stack_top()
            if Stack.pair[data] == top:
                if top == "}":
                    self.stack.append(data)
                    continue
                self.stack.pop()
                continue

            self.stack.append(data)

    def out_stack(self):
        """ 스택 계산하기 """
        while self.stack:
            before = self.stack.pop()
            if before == "{":
                self.count += 1
                bbefore = self.stack.pop()
                if bbefore == "{":
                    continue
                self.count += 1

            elif before == "}":
                bbefore = self.stack.pop()
                if bbefore == "}":
                    self.count += 1
                    continue

    def _stack_top(self):
        """ 스택 맨위 """
        return self.stack[-1]

    def _stack_empty(self):
        """ 스택 비었는지 확인하기 """
        if self.stack:
            return False
        return True

    def show_stack(self):
        """ 스택 확인하기 """
        print(self.stack)

    def answer(self, num):
        """ 정답 확인 """
        print(f"{num}. {self.count}")


class P:

    def run(self) -> None:
        count = 0
        while string := input.readline().strip():
            count += 1
            if string[0] == "-": break
            S = Stack(string)
            S.input_stack()
            S.out_stack()
            S.answer(count)

if __name__ == '__main__':
    # input = open('./4889.txt')
    P = P()
    P.run()