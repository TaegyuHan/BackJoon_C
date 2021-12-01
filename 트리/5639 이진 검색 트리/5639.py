from sys import stdin as input

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

class P5639:
    def __init__(self):
        self.root_node = 0

    def _make_root_node(self):
        self.root_node = Node(int(input.readline()))

    def _input_node(self):
        input_data = input.readline().rstrip()
        if input_data == "":
            return False

        comparison_node = self.root_node
        input_node = Node(int(input_data))

        while True:

            if comparison_node.item > input_node.item:
                if comparison_node.left == None:
                    comparison_node.left = input_node
                    break
                else:
                    comparison_node = comparison_node.left

            if comparison_node.item < input_node.item:
                if comparison_node.right == None:
                    comparison_node.right = input_node
                    break
                else:
                    comparison_node = comparison_node.right

        return True

    def _show_all_node(self, Node):
        if Node.left == None and Node.right == None:
            print(Node.item)
            return
        if Node.left:
            self._show_all_node(Node.left)
        if Node.right:
            self._show_all_node(Node.right)
        print(Node.item)

    def result(self):
        self._make_root_node()
        while self._input_node():
            pass

        self._show_all_node(self.root_node)

if __name__ == "__main__":
    # input = open("./5639.txt")
    P = P5639()
    P.result()
