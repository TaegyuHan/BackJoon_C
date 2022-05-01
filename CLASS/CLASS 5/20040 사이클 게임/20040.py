"""
    Solution code for "BaekJoon 사이클 게임"

    - Problem link: https://www.acmicpc.net/problem/20040
"""

from sys import stdin as input


class S:
    """ 상태 """
    INPUT = False
    NO_INPUT = True


class D:
    """ 데이터 """
    # 노드
    NODE_COUNT: int
    NODES_DIRECTION: list[int]

    # 엣지
    EDGE_COUNT: int

    # 정답
    answer: int


class P:

    def __init__(self) -> None:
        D.NODE_COUNT, D.EDGE_COUNT = map(int, input.readline().split())
        D.NODES_DIRECTION = [node_direction for node_direction in range(D.NODE_COUNT)]
        D.NODES_FIRST_INPUT_CHECK = [S.NO_INPUT for _ in range(D.NODE_COUNT)]

    def _find(self, node):
        """ 부모 찾기 """
        pnode = node
        while pnode != D.NODES_DIRECTION[pnode]:
            pnode = D.NODES_DIRECTION[pnode]

        D.NODES_DIRECTION[node] = pnode
        return pnode

    def _union(self, node1, node2):
        """ 합치기 """
        pnode1 = self._find(node1)
        pnode2 = self._find(node2)

        if pnode1 < pnode2:
            D.NODES_DIRECTION[pnode2] = pnode1
        else:
            D.NODES_DIRECTION[pnode1] = pnode2

    def run(self) -> None:
        D.answer = 0
        for _ in range(D.EDGE_COUNT):
            D.answer += 1
            node1, node2 = map(int, input.readline().split())

            if self._find(node1) == self._find(node2):
                print(D.answer)
                exit()

            self._union(node1, node2)

        print(0)

if __name__ == '__main__':
    # input = open('./20040.txt')
    P = P()
    P.run()