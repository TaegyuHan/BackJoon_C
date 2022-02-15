"""Solution code for "BaekJoon 부분수열의 합".

- Problem link: https://www.acmicpc.net/problem/1182
"""

from sys import stdin as input


class P:

    def __init__(self) -> None:
        self.N, self.S = map(int, input.readline().split())
        self.nums = list(map(int, input.readline().split()))
        self.answer = 0

    def _DFS(self, index: int, visited: list[int]) -> None:
        if index == self.N:
            if not visited:
                return
            if sum(visited) == self.S:
                self.answer += 1
            return
        self._DFS(index + 1, visited)

        visited.append(self.nums[index])
        self._DFS(index + 1,visited)
        visited.pop()


    def result(self) -> None:
        self._DFS(index=0, visited=[])
        print(self.answer)

if __name__ == '__main__':
    # input = open('./1182.txt')
    P = P()
    P.result()