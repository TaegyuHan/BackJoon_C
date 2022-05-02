"""
    Solution code for "BaekJoon 과제는 끝나지 않아".

    - Problem link: https://www.acmicpc.net/problem/17952
"""

from sys import stdin as input


class P:

    def run(self) -> None:
        input_count = int(input.readline())
        stack = []
        answer = 0
        for _ in range(input_count):
            check, *data = map(int, input.readline().split())

            # 1이면 데이터 넣기
            if check: stack.append(data)

            # 데이터 존재하면
            if stack:
                stack[-1][-1] -= 1 # 1 제거

                # 시간 0이면 제거
                if stack[-1][-1] == 0:
                    data = stack.pop()
                    answer += data[0]

        print(answer)

if __name__ == '__main__':
    # input = open('./17952.txt')
    P = P()
    P.run()