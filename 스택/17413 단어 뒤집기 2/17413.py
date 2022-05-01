"""
    Solution code for "BaekJoon 단어 뒤집기".

    - Problem link: https://www.acmicpc.net/problem/17413
"""

from sys import stdin as input

class S:
    """ 스택 활용 """
    OPEN = "<"
    CLOSE = ">"
    SPACE = " "

class Stack:
    """ 스택 """
    stack = []
    append_check = True

    @staticmethod
    def stack_init():
        """ 스택 초기화 """
        Stack.stack = []

    @staticmethod
    def get_reverse():
        """ 스택 내용 뒤집어서 출력 """
        string = ""
        while Stack.stack:
            string += Stack.stack.pop()
        return string

class P:

    def run(self) -> None:
        string = input.readline().strip()
        answer = ""

        for data in string:

            # 괄호 안의 데이터
            if not Stack.append_check:
                answer += data
                if data == S.CLOSE:
                    Stack.append_check = True
                continue

            # 괄호 열기
            if data == S.OPEN:
                Stack.append_check = False
                answer += Stack.get_reverse() + data
                Stack.stack_init()

            # 공백
            elif data == S.SPACE:
                answer += Stack.get_reverse() + data
                Stack.stack_init()

            # 괄호 밖의 데이터
            else:
                Stack.stack.append(data)

        answer += Stack.get_reverse()

        print(answer)

if __name__ == '__main__':
    # input = open('./17413.txt')
    P = P()
    P.run()