"""
    Solution code for "BaekJoon 압축".

    - Problem link: https://www.acmicpc.net/problem/1662
"""
from sys import stdin as input

class P:

    def run(self) -> None:
        string = input.readline()
        answer = 0
        for index, num in enumerate(string):
            if num == ")":
                tmp_count = answer
                for i in range(index, -1, -1):
                    if string[i] == "(": break
                    tmp_count += 1
                (i - 1) * tmp_count
            answer += 1
        print(answer)

if __name__ == '__main__':
    input = open('./1662.txt')
    P = P()
    P.run()