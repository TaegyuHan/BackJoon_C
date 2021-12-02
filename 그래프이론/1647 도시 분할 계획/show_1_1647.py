from sys import stdin as input

class P1647:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.edge_cnt = 0
        self.parent = []
        self.edges = []
        self.answer = 0

    def input_data(self):
        self.N, self.M = map(int, input.readline().split())
        self.parent = [i for i in range(0, self.N + 1)]

        for _ in range(self.M):
            self.edges.append(tuple(map(int, input.readline().split())))
            self.edges.sort(key=lambda x:x[2])

    def get_parent(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.get_parent(self.parent[a])
        return self.parent[a]

    # 합치기
    def union_parent(self, a_p, b_p):
        if a_p < b_p:
            self.parent[b_p] = a_p
        else:
            self.parent[a_p] = b_p

    def result(self):
        # MST 생성
        for edge in self.edges:
            # 다채우면 종료
            if self.edge_cnt + 2 == self.N:
                break
            ns, nd, nc = edge
            parent_s = self.get_parent(ns)
            parent_d = self.get_parent(nd)

            # 사이클 탐지
            if parent_s == parent_d:
                continue

            # 합치기
            self.union_parent(parent_s, parent_d)
            self.answer += nc
            self.edge_cnt += 1

        print(self.answer)

if __name__ == '__main__':
    # input = open("./1647.txt")
    P =  P1647()
    P.input_data()
    P.result()
