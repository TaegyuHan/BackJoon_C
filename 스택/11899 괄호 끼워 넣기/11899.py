"""
    Solution code for "BaekJoon 괄호 끼워넣기".

    - Problem link: https://www.acmicpc.net/problem/11899
"""
from sys import stdin as input


class P:

    def run(self) -> None:
        datas = input.readline()
        stack = []

        for data in datas:

            if not stack:
                stack.append(data)
            elif data == "(":
                stack.append(data)
            elif data == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(data)

        print(len(stack))


if __name__ == '__main__':
    # input = open('./11899.txt')
    P = P()
    P.run()