from sys import stdin as input

class P1922:
    def __init__(self):
        self.node_cnt = 0
        self.edge_cnt = 0
        self.edge_list = []
        self.union_find_list = []
        self.answer = 0

    def input_data(self):
        self.node_cnt = int(input.readline())
        for i in range(self.node_cnt + 1):
            self.union_find_list.append(i)

        self.edge_cnt = int(input.readline())
        for _ in range(self.edge_cnt):
            self.edge_list.append(tuple(map(int, input.readline().split())))
        self.edge_list.sort(key=lambda x:x[2])

    def _find_root(self, node):
        if self.union_find_list[node] != node:
            self.union_find_list[node] = self._find_root(self.union_find_list[node])
        return self.union_find_list[node]

    def _find_edge(self):
        for node1, node2, cost in self.edge_list:
            node1_root = self._find_root(node1)
            node2_root = self._find_root(node2)
            if node1_root == node2_root:
                continue

            if node1_root < node2_root:
                self.union_find_list[node2_root] = node1_root
            else:
                self.union_find_list[node1_root] = node2_root

            self.answer += cost

    def result(self):
        self._find_edge()
        print(self.answer)


if __name__ == '__main__':
    input = open("./1922.txt")
    P = P1922()
    P.input_data()
    P.result()
