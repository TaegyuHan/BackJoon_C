from itertools import combinations
from sys import stdin as input

class P:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    def __init__(self) -> None:
        self.L, self.C = map(int, input.readline().split())
        self.alphabets = input.readline().split()

    def result(self) -> None:
        for password in combinations(sorted(self.alphabets), self.L):
            vowel_count = sum(1 for alpa in password if alpa in P.VOWELS)
            if 1 <= vowel_count <= self.L - 2:
                print("".join(password))

if __name__ == '__main__':
    # input = open('./1759.txt')
    P = P()
    P.result()