from sys import stdin as input
from sys import setrecursionlimit
setrecursionlimit(300_000)

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

class P2957:
    def __init__(self):
        self.root_node = None
        self.cnt = 0

    def input_data(self):
        self.node_cnt = int(input.readline())

    def _insert(self, p_node, item):
        self.cnt += 1
        if p_node.item > item:
            if p_node.left == None:
                p_node.left = Node(item)
            else:
                self._insert(p_node.left, item)
        else:
            if p_node.right == None:
                p_node.right = Node(item)
            else:
                self._insert(p_node.right, item)

    def result(self):
        for _ in range(self.node_cnt):
            if self.root_node == None:
                self.root_node = Node(int(input.readline()))
                print(self.cnt)
                continue
            self._insert(self.root_node, int(input.readline()))
            print(self.cnt)


if __name__ == "__main__":
    # input = open("./2957.txt")
    P = P2957()
    P.input_data()
    P.result()
