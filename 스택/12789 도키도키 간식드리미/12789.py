"""
    Solution code for "BaekJoon 도키도키 간식드리미".

    - Problem link: https://www.acmicpc.net/problem/12789
"""
from sys import stdin as input


class P:


    def run(self) -> None:
        count = int(input.readline())
        people = list(map(int, input.readline().split()))
        people.reverse()
        stack = []

        number = 1
        while people or stack:

            # 스택에 사람이 있을때는
            if stack and stack[-1] == number:
                stack.pop()
                number += 1
                continue

            if not people: break
            man_number = people.pop()

            if number == man_number:
                number += 1
                continue

            stack.append(man_number)

        if stack:
            print("Sad")
        else:
            print("Nice")


if __name__ == '__main__':
    # input = open('./12789.txt')
    P = P()
    P.run()