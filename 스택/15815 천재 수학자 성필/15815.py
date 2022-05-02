"""
    Solution code for "BaekJoon 천재 수학자 성필".

    - Problem link: https://www.acmicpc.net/problem/15815
"""

from sys import stdin as input


class Sign:
    """ 부호 """
    ADD = "+"
    SUB = "-"
    DIV = "/"
    MUL = "*"


class P:

    def run(self) -> None:
        string = input.readline().strip()
        stack = []
        for data in string:

            if data.isnumeric():
                stack.append(int(data))
                continue

            num1, num2 = stack.pop(), stack.pop()
            if data == Sign.ADD:
                stack.append(num2 + num1)
            elif data == Sign.SUB:
                stack.append(num2 - num1)
            elif data == Sign.DIV:
                stack.append(num2 // num1)
            elif data == Sign.MUL:
                stack.append(num2 * num1)

        print(stack.pop())


if __name__ == '__main__':
    # input = open('./15815.txt')
    P = P()
    P.run()