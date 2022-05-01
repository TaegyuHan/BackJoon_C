"""
    Solution code for "BaekJoon 후위 표기식2".

    - Problem link: https://www.acmicpc.net/problem/1935
"""

from sys import stdin as input


class Sign:
    """ 신호 """
    PLUS = "+"
    MINUS = "-"
    DIV = "/"
    MUL = "*"


class Stack:
    """ 스택 """
    ALPHABET_COUNT: int
    STRING: str
    ALPHABET_VALUES = []
    stack = []
    answer = 0
    tmp = 0

    @staticmethod
    def alpha_value(alphabet):
        """ 알파벳 값 """
        return Stack.ALPHABET_VALUES[ord(alphabet) - 65]

    @staticmethod
    def pop_two():
        return Stack.stack.pop(), Stack.stack.pop()

    @staticmethod
    def answer():
        """ 정답 """
        print(f'{Stack.stack.pop():.2f}')


class P:

    def _input_data(self):
        """ 데이터 받기 """
        Stack.ALPHABET_COUNT = int(input.readline())
        Stack.STRING = input.readline().strip()
        Stack.ALPHABET_VALUES = [int(input.readline()) for _ in range(Stack.ALPHABET_COUNT)]

    def run(self) -> None:
        self._input_data()

        # 계산하기
        for data in Stack.STRING:

            # 알파벳 스택에 저장
            if data.isalpha():
                Stack.stack.append(Stack.alpha_value(data))
                continue

            num1, num2 = Stack.pop_two()
            if data == Sign.MUL:
                Stack.stack.append(num2 * num1)
            elif data == Sign.DIV:
                Stack.stack.append(num2 / num1)
            elif data == Sign.PLUS:
                Stack.stack.append(num2 + num1)
            elif data == Sign.MINUS:
                Stack.stack.append(num2 - num1)

        Stack.answer()


if __name__ == '__main__':
    # input = open('./1935.txt')
    P = P()
    P.run()