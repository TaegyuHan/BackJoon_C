"""
    Solution code for "BaekJoon 트리의 지름".

    - Problem link: https://www.acmicpc.net/problem/1967
"""
from sys import stdin as input
# input = open('./1967.txt')


class D:
    """ 데이터 """
    NODE_COUNT = int(input.readline())
    if NODE_COUNT == 1:
        print(0)
        exit()

    GRAPH = {}
    ANSWER = 0
    long_node = 0
    for _ in range(NODE_COUNT - 1):
        n1, n2, weight = map(int, input.readline().split())
        if n1 not in GRAPH: GRAPH[n1] = []
        if n2 not in GRAPH: GRAPH[n2] = []
        GRAPH[n1].append((n2, weight))
        GRAPH[n2].append((n1, weight))

class P:

    def _DFS(self, snode, weight):
        """ 우선 깊이 탐색 """
        visited = set()
        stack = [(snode, weight)]

        while stack:
            cnode, cweight = stack.pop()
            if cnode in visited: continue
            visited.add(cnode)

            if len(D.GRAPH[cnode]) == 1 and cweight > D.ANSWER:
                D.ANSWER = cweight
                D.long_node = cnode

            for nnode, nweight in D.GRAPH[cnode]:
                if nnode in visited: continue
                stack.append((nnode, cweight + nweight))

    def run(self) -> None:
        self._DFS(1, 0)
        self._DFS(D.long_node, 0)
        print(D.ANSWER)


if __name__ == '__main__':
    P = P()
    P.run()