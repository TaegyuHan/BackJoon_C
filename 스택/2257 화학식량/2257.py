"""
    Solution code for "BaekJoon 화학식량".

    - Problem link: https://www.acmicpc.net/problem/2257

    첫째 줄에 화학식이 주어진다.
    화학식은 H, C, O, (, ), 2, 3, 4, 5, 6, 7, 8, 9만으로 이루어진 문자열이며
    그 길이는 100을 넘지 않는다.
"""
from sys import stdin as input


class S:
    OPEN = "("
    CLOSE = ")"


class P:

    def run(self) -> None:
        sign = {
            "H": 1,
            "C": 12,
            "O": 16,
        }

        string = input.readline().strip()
        stack = []
        for data in string:

            # 열린 괄호
            if data == S.OPEN:
                stack.append(data)

            # 문자를 만났을 경우
            elif data.isalpha():
                stack.append(sign[data])

            # 숫자를 만났을 경우
            elif data.isnumeric():
                stack[-1] *= int(data)

            # 닫힌 괄호 만났을 경우
            elif data == S.CLOSE:
                tmp = 0
                while True:
                    stack_data = stack.pop()
                    if stack_data == S.OPEN: break
                    tmp += stack_data
                stack.append(tmp)

        print(sum(stack))


if __name__ == '__main__':
    # input = open('./2257.txt')
    P = P()
    P.run()