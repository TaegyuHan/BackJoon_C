"""
    Solution code for "BaekJoon 좋은 단어".

    - Problem link: https://www.acmicpc.net/problem/
"""

from sys import stdin as input


class D:
    """ 데이터 """
    TEST_CASE: int


class Stack:

    def __init__(self, string):
        self._string = string
        self._stack = []

    def _empty_check(self):
        """ 빈 스택 확인 """
        if not len(self._stack):
            return True
        return False

    def _stack_top(self):
        """ 스택 맨 위 확인 """
        return self._stack[-1]

    def check_good_word(self):
        """ 좋은 단어 """
        for data in self._string:
            # 스택이 비어있으면
            if self._empty_check():
                self._stack.append(data)
                continue
                
            before = self._stack_top()
            if before == data:
                self._stack.pop()
            elif before != data:
                self._stack.append(data)

        if not self._stack:
            return 1
        return 0


class P:

    def run(self) -> None:
        answer = 0
        D.TEST_CASE = int(input.readline())
        for _ in range(D.TEST_CASE):
            stack = Stack(input.readline().strip())
            answer += stack.check_good_word()
        print(answer)


if __name__ == '__main__':
    # input = open('./3986.txt')
    P = P()
    P.run()