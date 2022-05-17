"""
    Solution code for "BaekJoon 이분 그래프".

    - Problem link: https://www.acmicpc.net/problem/1707
"""
from sys import stdin as input
from collections import deque


class S:
    """ 상태 """
    NO_COLOR = 0
    RED = 1
    BLUE = 2


class D:
    """ 데이터 """
    TEST_CASE: int
    NODE: int
    EDEG: int
    node_table = {}


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _input_data(self):
        """ 데이터 받기 """
        tmp = {}
        D.NODE, D.EDGE = map(int, input.readline().strip().split())
        for _ in range(D.EDGE):
            node1, node2 = input.readline().strip().split()
            if not node1 in tmp: tmp[node1] = []
            if not node2 in tmp: tmp[node2] = []
            tmp[node1].append(node2)
            tmp[node2].append(node1)
        D.node_table = tmp

    def _bipartite_graph(self):
        """ 이분 그래프 """
        visited = [S.NO_COLOR for _ in range(D.NODE + 1)]

        for i in range(1, D.NODE + 1):
            if visited[i]: continue
            elif str(i) not in D.node_table.keys(): continue
            q = deque([str(i)])

            while q:
                cnode = q.popleft()
                cnode_index = int(cnode)
                # 이미 방문한 노드인지 확인
                if not visited[cnode_index]: visited[cnode_index] = S.RED

                # 다음 노드 색 정하기
                if visited[cnode_index] == S.RED: ncolor = S.BLUE
                elif visited[cnode_index] == S.BLUE: ncolor = S.RED

                for nnode in D.node_table[cnode]:
                    # 이미 방문한 노드
                    nnode_index = int(nnode)
                    if visited[nnode_index]:
                        # 이분 그래프 색 맞음
                        if visited[nnode_index] == ncolor: continue
                        # 틀림
                        return "NO"
                    # 처음 방문한 노드
                    visited[nnode_index] = ncolor
                    q.append(nnode)
        return "YES"

    def run(self) -> None:
        for _ in range(D.TEST_CASE):
            self._input_data()
            print(self._bipartite_graph())


if __name__ == '__main__':
    # input = open('./1707.txt')
    P = P()
    P.run()