"""
    Solution code for "BaekJoon 파일 정리".

    - Problem link: https://www.acmicpc.net/problem/20291
"""
from collections import defaultdict
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./20291.txt')


class D:
    """ 데이터 """
    COUNT = int(input.readline())
    file_count = defaultdict(int)

    @staticmethod
    def input_file_data():
        """ 파일 데이터 받기 """
        for _ in range(D.COUNT):
            name, extension = input.readline().strip().split(".")
            D.file_count[extension] += 1

    @staticmethod
    def show_files():
        """ 파일 보여주기 """
        for extension in sorted(D.file_count.keys()):
            print(extension, D.file_count[extension])


class P:

    def run(self) -> None:
        D.input_file_data()
        D.show_files()

if __name__ == '__main__':
    P = P()
    P.run()