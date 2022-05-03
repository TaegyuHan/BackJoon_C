"""Solution code for "BaekJoon 오등큰수".

- Problem link: https://www.acmicpc.net/problem/17299
"""

from sys import stdin as input

class S:
    """ 상태 """
    NO_UP_NUMBER = -1

class P:

    def run(self) -> None:
        # 데이터 받기
        num_count = int(input.readline().strip())
        nums = list(map(int, input.readline().split()))
        answer_list = [S.NO_UP_NUMBER for _ in range(num_count)]
        stack = []

        # 숫자 수 계산하기
        count = {}
        for num in nums:
            if not num in count:
                count[num] = 1
                continue
            count[num] += 1

        # stack에 넣기
        for index, num in enumerate(nums):
            # 스택이 비어있는 경우
            if not stack:
                stack.append((index, -1, num))

            # 스택이 안비어 있는 경우
            else:
                while stack:
                    if count[stack[-1][-1]] >= count[num]: break
                    tindex, _, big_num = stack.pop()
                    answer_list[tindex] = num
                stack.append((index, -1, num))
                
        print(*answer_list)

if __name__ == '__main__':
    # input = open('./17299.txt')
    P = P()
    P.run()