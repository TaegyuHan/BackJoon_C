"""
    Solution code for "BaekJoon 트리의 지름".

    - Problem link: https://www.acmicpc.net/problem/1167
"""
from sys import stdin as input
# input = open('./1167.txt')


class D:
    """ 데이터 """
    NODE_COUNT = int(input.readline())
    long_node = 0 # 가장 긴 길이를 가진 노드
    maximum = 0 # 최대 길이

    # 그래프 데이터 넣기
    GRAPH = {}
    for _ in range(NODE_COUNT):
        key_node, *nodes, end = list(map(int, input.readline().split()))
        GRAPH[key_node] = []
        for i in range(0, len(nodes), 2):
            GRAPH[key_node].append(tuple(nodes[i:i + 2]))


class P:

    def _DFS(self, snode, weight):
        """ BFS 알고리즘 """
        visited = set()
        stack = [(snode, weight)]
        while stack:
            cnode, cweight = stack.pop()
            if cnode in visited: continue
            visited.add(cnode)

            if len(D.GRAPH[cnode]) == 1 and cweight > D.maximum:
                D.maximum, D.long_node = cweight, cnode

            for nnode, nweight in D.GRAPH[cnode]:
                if nnode in visited: continue
                stack.append((nnode, nweight + cweight))

    def run(self) -> None:
        self._DFS(1, 0)
        self._DFS(D.long_node, 0)
        print(D.maximum)


if __name__ == '__main__':
    P = P()
    P.run()