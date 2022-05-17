"""
    Solution code for "BaekJoon 탑".

    - Problem link: https://www.acmicpc.net/problem/2493
"""

from sys import stdin as input


class P:

    def run(self) -> None:
        top_count = int(input.readline())
        answer_list = [0 for _ in range(top_count)]
        stack = []

        for index, top in enumerate(map(int, input.readline().split())):
            # 스택에 데이터 없는 경우
            if not stack:
                stack.append((index, top))

            # 현재 탑이 작아서 레이저를 만나는 경우
            elif stack[-1][-1] >= top:
                answer_list[index] = stack[-1][0] + 1
                stack.append((index, top))

            else:
                # 현재 탑이 더 큰경우
                while stack:
                    if stack[-1][-1] > top:
                        answer_list[index] = stack[-1][0] + 1
                        break
                    stack.pop()

                stack.append((index, top))

        print(*answer_list)


if __name__ == '__main__':
    # input = open('./2493.txt')
    P = P()
    P.run()