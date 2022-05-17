"""
    Solution code for "BaekJoon 오큰수".

    - Problem link: https://www.acmicpc.net/problem/17298
"""

from sys import stdin as input


class P:

    def run(self) -> None:
        input_data_count = int(input.readline())
        answer_list = [0 for _ in range(input_data_count)]
        stack = []
        for index, data in enumerate(map(int, input.readline().split())):
            if not stack:
                stack.append((index, -1, data))
                continue

            # 데이터가 있는경우
            while stack:
                if stack[-1][-1] >= data: break
                answer_index, _, _ = stack.pop()
                answer_list[answer_index] = data
            stack.append((index, -1, data))

        # 오큰수가 없는 숫자
        while stack:
            index, data, _ = stack.pop()
            answer_list[index] = data

        print(*answer_list)

if __name__ == '__main__':
    # input = open('./17298.txt')
    P = P()
    P.run()
