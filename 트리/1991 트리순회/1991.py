from sys import stdin as input
# input = open("./1991.txt")

class TreeTraversal:
    def __init__(self):
        self.node_count = 0
        self.node_list = {}
        self.preorder = []
        self.inorder = []
        self.postorder = []

    def input_data(self, NC):
        for _ in range(NC):
            node, left, right = input.readline().rstrip().split()
            self.node_list[node] = [left, right]

    def traversal(self, node):
        if node == '.':
            return

        left, right = self.node_list[node]
        self.preorder.append(node)
        if left != ".":
            self.traversal(left)
        self.inorder.append(node)
        if right != ".":
            self.traversal(right)
        self.postorder.append(node)
        return

    def result(self):
        self.traversal("A")
        print("".join(self.preorder))
        print("".join(self.inorder))
        print("".join(self.postorder))

TB = TreeTraversal()
TB.input_data(int(input.readline()))
TB.result()
