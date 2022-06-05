"""
    Solution code for "BaekJoon 트리".

    - Problem link: https://www.acmicpc.net/problem/4803
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./4803.txt')


class D:
    """ 데이터 """
    node_count = 0
    edge_count = 0
    parent_nodes = []
    tset_count = 0
    NO_TREE = 0

    @staticmethod
    def stop_check():
        """ 테스트 실행 확인 """
        D.node_count, D.edge_count = map(int, input.readline().split())
        return D.node_count or D.edge_count

    @staticmethod
    def data_init():
        """ 데이터 초기화 """
        D.parent_nodes = [0] + [node for node in range(1, D.node_count + 1)]


class P:

    def union(self, node1, node2):
        """ 합집합 """
        parent_node1 = self.find(node1)
        parent_node2 = self.find(node2)

        if parent_node1 > parent_node2:
            D.parent_nodes[parent_node1] = parent_node2
            return True
        elif parent_node1 < parent_node2:
            D.parent_nodes[parent_node2] = parent_node1
            return True
        else:
            D.parent_nodes[parent_node2] = D.NO_TREE
            D.parent_nodes[parent_node1] = D.NO_TREE

    def find(self, node):
        """ root 노드 설정 """
        if D.parent_nodes[node] == node:
            return node

        D.parent_nodes[node] = self.find(D.parent_nodes[node])
        return D.parent_nodes[node]

    def _edge_union(self):
        """ edge 합치기 """
        for _ in range(D.edge_count):
            node1, node2 = map(int, input.readline().split())
            self.union(node1, node2)

        # find 초기화
        for node in range(1, D.node_count + 1):
            self.find(node)

        # 결과
        tree_count = len(set(D.parent_nodes)) - 1
        if tree_count == 0:
            print(f"Case {D.tset_count}: No trees.")

        # 트리인 경우
        elif tree_count == 1:
            print(f"Case {D.tset_count}: There is one tree.")
        else:
            print(f"Case {D.tset_count}: A forest of {tree_count} trees.")

    def run(self) -> None:
        """ 실행 """
        while D.stop_check():
            D.tset_count += 1
            D.data_init()
            self._edge_union()


if __name__ == '__main__':
    P = P()
    P.run()