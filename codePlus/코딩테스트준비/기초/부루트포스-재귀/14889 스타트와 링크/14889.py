"""Solution code for "Problem Number 14889. 스타트와 링크".

- Problem link: https://www.acmicpc.net/problem/14889
"""

from sys import stdin as input
from itertools import combinations

class P:

    def __init__(self):
        self.N = int(input.readline())
        self.board = [list(map(int, input.readline().split()))
                      for _ in range(self.N)]

    def main(self):
        self.answer = 100
        self.man = set(i for i in range(self.N))

        for team in combinations(range(self.N), self.N//2):
            team_sum, other_team_sum = 0, 0
            other_team = self.man - set(team)

            for x, y in combinations(team, 2):
                team_sum += self.board[x][y] + self.board[y][x]

            for x, y in combinations(other_team, 2):
                other_team_sum += self.board[x][y] + self.board[y][x]

            self.answer = min(self.answer, abs(team_sum - other_team_sum))

        print(self.answer)

if __name__ == '__main__':
    # input = open("./14889.txt")
    P = P()
    P.main()