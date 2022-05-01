"""
    Solution code for "BaekJoon 후위 표기식".

    - Problem link: https://www.acmicpc.net/problem/1918
"""
from sys import stdin as input


class S:
    """ 부호 """
    PLUS = "+"
    MINUS = "-"
    PM = (PLUS, MINUS)

    DIV = "/"
    MUL = "*"
    DM = (DIV, MUL)

    OPEN = "("
    CLOSE = ")"
    OC = (OPEN, CLOSE)

    ALL = PM + DM + OC

    LIST_END = -1


class D:
    """ STRING """
    STRING: str


class SignStack:
    """ 기호 스택 """
    data = []

    @staticmethod
    def append(x):
        SignStack.data.append(x)

    @staticmethod
    def pop():
        return SignStack.data.pop()

    @staticmethod
    def empty():
        if not SignStack.data:
            return True
        return False

    @staticmethod
    def check():
        return SignStack.data[-1]

    @staticmethod
    def close():
        for i in range(len(SignStack.data) - 1, -1, -1):
            yield SignStack.data.pop()

    @staticmethod
    def range():
        for _ in range(len(SignStack.data)):
            yield SignStack.data.pop()


class P:

    def __init__(self) -> None:
        D.STRING = input.readline().strip()

    def run(self) -> None:
        answer, *string = D.STRING
        for num_or_sign in string:

            if SignStack.empty() and num_or_sign in S.ALL:
                SignStack.append(num_or_sign)
                continue

            elif num_or_sign == S.OPEN:
                SignStack.append(num_or_sign)
                continue

            elif num_or_sign == S.CLOSE:
                for sign in SignStack.close():
                    if sign == S.OPEN: break
                    answer += sign
                continue

            elif num_or_sign == S.DIV:
                SignStack.append(num_or_sign)
                sign = SignStack.check()
                if sign in S.DM:
                    answer += SignStack.pop()
                continue

            elif num_or_sign == S.MUL:
                SignStack.append(num_or_sign)
                sign = SignStack.check()
                if sign in S.DM:
                    answer += SignStack.pop()
                continue

            elif num_or_sign == S.PLUS:
                sign = SignStack.check()
                if sign in S.PM:
                    SignStack.append(num_or_sign)
                if sign in S.DM:
                    for sign in SignStack.range():
                        answer += sign
                    continue
                continue

            elif num_or_sign == S.MINUS:
                sign = SignStack.check()
                if sign in S.PM:
                    SignStack.append(num_or_sign)
                if sign in S.DM:
                    for sign in SignStack.range():
                        answer += sign
                    continue
                continue

            answer += num_or_sign

        for sign in SignStack.range():
            answer += sign

        print(answer)


if __name__ == '__main__':
    input = open('1918.txt')
    P = P()
    P.run()