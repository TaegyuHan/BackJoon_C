"""
    Solution code for "BaekJoon 트리".

    - Problem link: https://www.acmicpc.net/problem/1068
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./1068.txt')


class D:
    """ 데이터 """
    NODE_COUNT: int
    NODES = {}
    PARENT_NODES = []
    DELETE_NODE: int
    DONT_HAVE_PNODE = -1
    leaf_count = []
    root_node = []


class P:

    def __init__(self) -> None:
        """ 데이터 받기 """
        D.NODE_COUNT = int(input.readline())
        D.NODES = {node: [] for node in range(D.NODE_COUNT)}

        # 노드 데이터 넣기
        for cnode, pnode in enumerate(map(int, input.readline().split())):
            D.leaf_count.append(0)
            D.PARENT_NODES.append(pnode)
            if pnode == D.DONT_HAVE_PNODE:
                D.root_node.append(cnode)
                continue
            D.NODES[pnode].append(cnode)

        D.DELETE_NODE = int(input.readline())

    def _find_leaf(self, node):
        """ 리프 노드 수 세기 """
        if not D.NODES[node]:
            D.leaf_count[node] = 1
            return 1

        leaf_sum = 0
        for cnode in D.NODES[node]:
            leaf_sum += self._find_leaf(cnode)
        D.leaf_count[node] = leaf_sum
        return leaf_sum

    def run(self) -> None:
        """ 실행 """
        leaf_all = 0
        for rnode in D.root_node:
            leaf_all += self._find_leaf(rnode)

        answer = leaf_all - D.leaf_count[D.DELETE_NODE]
        if D.PARENT_NODES[D.DELETE_NODE] != -1 \
                and len(D.NODES[D.PARENT_NODES[D.DELETE_NODE]]) == 1:
            answer += 1
        print(answer)


if __name__ == '__main__':
    P = P()
    P.run()