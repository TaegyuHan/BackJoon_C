"""
    Solution code for "BaekJoon 키로거".

    - Problem link: https://www.acmicpc.net/problem/
"""

from sys import stdin as input


class Key:
    """ 키 입력 """
    LEFT = "<"
    RIGHT = ">"
    DELETE = "-"


class D:
    """ 데이터 케이스 """
    TEST_CASE: int


class LeftStack:
    """ 왼쪽 스택 """
    stack = []

    @staticmethod
    def empty():
        """ 비었는지 확인 """
        if len(LeftStack.stack):
            return False
        return True


class RightStack:
    """ 오른쪽 스택 """
    stack = []

    @staticmethod
    def empty():
        """ 비었는지 확인 """
        if len(RightStack.stack):
            return False
        return True


class P:

    def _stack_init(self):
        """ 스택 초기화 """
        LeftStack.stack = []
        RightStack.stack = []

    def _left_to_right(self):
        """ 왼쪽 스택에서 오른쪽 스택으로 """

    def _right_to_left(self):
        """ 오른쪽 스택에서 왼쪽 스택으로 """

    def _test_run(self):
        """ 테스트 케이스 실행 """
        string = input.readline().strip()
        for data in string:

            if data == Key.LEFT:
                if LeftStack.empty(): continue
                RightStack.stack.append(LeftStack.stack.pop())

            elif data == Key.RIGHT:
                if RightStack.empty(): continue
                LeftStack.stack.append(RightStack.stack.pop())

            elif data == Key.DELETE:
                if LeftStack.empty(): continue
                LeftStack.stack.pop()
            # 데이터 받기
            else:
                LeftStack.stack.append(data)

    def _answer(self):
        """ 정답 확인하기 """
        while RightStack.stack:
            LeftStack.stack.append(RightStack.stack.pop())
        print("".join(map(str, LeftStack.stack)))

    def run(self) -> None:
        D.TEST_CASE = int(input.readline())
        for _ in range(D.TEST_CASE):
            self._stack_init()
            self._test_run()
            self._answer()

if __name__ == '__main__':
    # input = open('./5397.txt')
    P = P()
    P.run()