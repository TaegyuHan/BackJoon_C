"""
    Solution code for "BaekJoon 후위 표기식".

    - Problem link: https://www.acmicpc.net/problem/1918
"""

from sys import stdin as input


class S:

    OPEN = "("
    CLOSE = ")"

    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    ADD_SUB = (ADD, SUB)
    MUL_DIV = (MUL, DIV)


class P:

    def __init__(self) -> None:
        self.stack = []

    def stack_top(self):
        """ 스택 맨위 값 """
        return self.stack[-1]

    def run(self) -> None:
        string = input.readline().strip()
        answer = ""

        for data in string:

            if data.isalpha():
                answer += data

            elif not self.stack:
                self.stack.append(data)

            elif data in S.ADD_SUB:
                if self.stack_top() in S.MUL_DIV:
                    while self.stack:
                        if self.stack_top() == S.OPEN: break
                        answer += self.stack.pop()

                elif self.stack_top() in S.ADD_SUB:
                    answer += self.stack.pop()

                self.stack.append(data)

            elif data in S.MUL_DIV:
                if self.stack_top() in S.MUL_DIV:
                    answer += self.stack.pop()
                self.stack.append(data)

            elif data == S.OPEN:
                self.stack.append(data)

            elif data == S.CLOSE:
                while self.stack:
                    before = self.stack.pop()
                    if before == S.OPEN: break
                    answer += before

        while self.stack:
            answer += self.stack.pop()

        print(answer)

if __name__ == '__main__':
    # input = open('./1918.txt')
    P = P()
    P.run()