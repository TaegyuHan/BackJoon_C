"""
    Solution code for "BaekJoon 괄호의 값".

    - Problem link: https://www.acmicpc.net/problem/2504

    문제 풀이 ( 스택 )

    중괄호, 대괄호 들어옴

    1. ‘()’ 인 괄호열의 값은 2이다.
    2. ‘[]’ 인 괄호열의 값은 3이다.
    3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
    4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
    5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

"""
from sys import stdin as input


class S:
    """ 괄호 모양 """
    S_OPEN = "("
    S_CLOSE = ")"

    B_OPEN = "["
    B_CLOSE = "]"


class P:

    def __init__(self):
        """ 데이터 받기 """
        self._bracket = input.readline().strip()
        self._stack = []
        self._tmp = 1
        self._answer = 0

    def _exit(self):
        """ 프로그램 종료 """
        print(0)
        exit()

    def run(self) -> None:
        for i in range(len(self._bracket)):
            
            # 열렸을때
            if self._bracket[i] == S.S_OPEN:
                self._stack.append(self._bracket[i])
                self._tmp *= 2

            elif self._bracket[i] == S.B_OPEN:
                self._stack.append(self._bracket[i])
                self._tmp *= 3

            elif self._bracket[i] == S.S_CLOSE:
                if not self._stack or self._stack[-1] == S.B_OPEN:
                    self._exit()
                if self._bracket[i - 1] == S.S_OPEN:
                    self._answer += self._tmp
                self._stack.pop()
                self._tmp //= 2

            elif self._bracket[i] == S.B_CLOSE:
                if not self._stack or self._stack[-1] == S.S_OPEN:
                    self._exit()
                if self._bracket[i - 1] == S.B_OPEN:
                    self._answer += self._tmp
                self._stack.pop()
                self._tmp //= 3

        if self._stack:
            print(0)
        else:
            print(self._answer)


if __name__ == '__main__':
    # input = open('./2504.txt')
    P = P()
    P.run()