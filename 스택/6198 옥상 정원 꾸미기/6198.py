"""Solution code for "BaekJoon 옥상 정원 꾸미기".

- Problem link: https://www.acmicpc.net/problem/6198
"""

from sys import stdin as input


class P:

    def run(self) -> None:
        count = int(input.readline().strip())
        answer = 0
        stack = []

        for index in range(count):
            num = int(input.readline().strip())
            if not stack: # 스택이 비었을 경우
                stack.append(num)
                continue

            while stack:
                if stack[-1] > num:
                    answer += len(stack)
                    break
                stack.pop()
            stack.append(num)

        print(answer)

if __name__ == '__main__':
    # input = open('./6198.txt')
    P = P()
    P.run()