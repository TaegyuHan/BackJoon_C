"""
    Solution code for "BaekJoon 오아시스 재결합".

    - Problem link: https://www.acmicpc.net/problem/3015
"""

from sys import stdin as input


class S:
    TOP = -1


class P:

    def run(self) -> None:
        count = int(input.readline())
        result = 0
        stack = []

        for _ in range(count):
            num = int(input.readline())

            tmp_count = 1
            while stack:
                if stack[-1][0] < num:
                    result += stack.pop()[-1]
                    tmp_count = 1
                elif stack[-1][0] == num:
                    result += stack[-1][-1]
                    tmp_count = stack[-1][-1] + 1
                    stack.pop()
                else:
                    result += 1
                    break

            stack.append((num, tmp_count))

        print(result)

if __name__ == '__main__':
    # input = open('./3015.txt')
    P = P()
    P.run()