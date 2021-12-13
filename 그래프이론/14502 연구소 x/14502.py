from sys import stdin as input
from itertools import combinations

class P14502:

    def input_data(self):
        self.H, self.W = map(int, input.readline().split())
        self.zero_index = []
        for i in range(self.H):
            row = map(int, input.readline().split())
            for j, num in enumerate(row):
                if num == 0:
                    self.zero_index.append((i, j))

        self._combination_of_three(self.zero_index)

    def _combination_of_three(self, index_list):
        # 조합 개수 생성
        list(combinations(index_list, 3))
        print()


    def result(self):
        pass

if __name__ == '__main__':
    input = open("./14502.txt")
    P = P14502()
    P.input_data()
    P.result()