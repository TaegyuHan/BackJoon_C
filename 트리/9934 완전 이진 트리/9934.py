from sys import stdin as input


class CBTree:

    def __init__(self):
        self.node_height = 0
        self.node_number_list = []
        self.result_node_list = []

    def input_data(self, height):
        self.node_height = height
        self.node_number_list = list(input.readline().split())
        self.node_number_list.reverse()
        self.result_node_list = [[] for _ in range(height)]

    def recursive_search(self, height):
        if height > self.node_height - 1:
            return
        self.recursive_search(height + 1)
        self.result_node_list[height].append(self.node_number_list.pop())
        self.recursive_search(height + 1)

    def result(self):
        root_node_index = 0
        self.recursive_search(root_node_index)
        for H_node in self.result_node_list:
            print(" ".join(H_node))

if __name__ == '__main__':
    # input = open("./9934.txt")
    CBT = CBTree()
    CBT.input_data(int(input.readline()))
    CBT.result()
