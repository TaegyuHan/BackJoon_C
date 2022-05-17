"""
    Solution code for "BaekJoon 문자열 폭발".

    - Problem link: https://www.acmicpc.net/problem/9935
"""

from sys import stdin as input


class P:

    def run(self) -> None:
        string = input.readline().strip()
        match = input.readline().strip()
        stack = []

        match_count = 0
        for char in string:
            print(stack)
            stack.append(char)

            # 문자열 같은지 확인
            if match[match_count] != char: # 다른 경우
                if match[0] != char:
                    match_count = 1
                    continue
                match_count = 0

            # 같은 경우
            match_count += 1
            if len(match) == match_count: # 일치
                match_count = 0 # 초기화

                # 제거 해주기
                for _ in range(len(match)): stack.pop()

                # 폭발후 앞 문자와 같은지 확인
                if stack and stack[-1] == match[match_count]:
                    match_count += 1

        if stack:
            print("".join(stack))
        else:
            print("FRULA")


if __name__ == '__main__':
    input = open('./9935.txt')
    P = P()
    P.run()