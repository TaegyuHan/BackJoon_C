from sys import stdin as input

class FBTree:
    def __init__(self):
        self.node_height = 0
        self.node_edge = []

    def input_data(self):
        self.node_height = int(input.readline())
        nodes = list(map(int, input.readline().split()))

        for i in range(1, 1+self.node_height):
            edge, nodes = nodes[:2 ** i], nodes[2 ** i:]
            self.node_edge.append(edge)

    def result(self):
        print(self.node_edge)


if __name__ == '__main__':
    input = open("./13325.txt")
    FBT = FBTree()
    FBT.input_data()
    FBT.result()