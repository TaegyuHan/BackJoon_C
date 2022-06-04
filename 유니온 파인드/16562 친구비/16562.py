"""
    Solution code for "BaekJoon 친구비".

    - Problem link: https://www.acmicpc.net/problem/16562
"""
from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
# input = open('./16562.txt')


class D:
    """ 데이터 """
    prices = [0]
    parent_nodes = [0]


class P:

    def __init__(self):
        """ 데이터 받기 """
        D.NODE_COUNT, D.EDGE_COUNT, D.money = map(int, input.readline().split())
        D.prices += list(map(int, input.readline().split()))
        D.parent_nodes += [node for node in range(1, D.NODE_COUNT + 1)]

    def union(self, node1, node2):
        """ 합치기 """
        parent_node1 = self.find(node1)
        parent_node2 = self.find(node2)
        parent_node1_price = D.prices[parent_node1]
        parent_node2_price = D.prices[parent_node2]

        if parent_node1_price > parent_node2_price:
            D.parent_nodes[parent_node1] = parent_node2
        elif parent_node1_price < parent_node2_price:
            D.parent_nodes[parent_node2] = parent_node1
        else:
            if parent_node1 > parent_node2:
                D.parent_nodes[parent_node1] = parent_node2
            else:
                D.parent_nodes[parent_node2] = parent_node1

    def find(self, node):
        """ 찾기 """
        if D.parent_nodes[node] == node:
            return node

        D.parent_nodes[node] = self.find(D.parent_nodes[node])
        return D.parent_nodes[node]

    def run(self) -> None:
        """ 실행 """
        # edge 연동하기
        for _ in range(D.EDGE_COUNT):
            node1, node2 = map(int, input.readline().split())
            self.union(node1, node2)

        # root node 정리
        for node in range(D.NODE_COUNT):
            self.find(node)

        # 친구 금액 계산
        friend_price = sum(map(lambda x: D.prices[x],
                               set(D.parent_nodes)))

        if D.money >= friend_price:
            print(friend_price)
        else:
            print("Oh no")


if __name__ == '__main__':
    P = P()
    P.run()