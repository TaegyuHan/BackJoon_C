import sys
input = sys.stdin.readline

# 부모 찾기
def get_parent(parent, a):
    a_parent = a
    while True:
        if parent[a_parent] == a_parent:
            return a_parent
        else:
            a_parent = parent[a_parent]

# 합치기
def union_parent(parent, a_p, b_p):
    # 그 외 index 작은 순
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

# edge
class Edge:
    def __init__(self, src, dst, cost):
        self.src = src
        self.dst = dst
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

# input
n, m = map(int,input().split())
parent = [i for i in range(0,n+1)]
edges= []
edge_cnt , answer = 0, 0

# main
# input 처리
for _ in range(m):
    src, dst, cost = map(int,input().split())
    edge = Edge(src,dst,cost)
    edges.append(edge)

edges.sort()

# MST 생성
for edge in edges:

    # 다채우면 종료
    if edge_cnt + 2 == n:
        break

    # 사이클 탐지
    if get_parent(parent, edge.src) == get_parent(parent, edge.dst):
        continue

    # 합치기
    union_parent(parent, get_parent(parent, edge.src), get_parent(parent, edge.dst))
    answer += edge.cost
    edge_cnt += 1

print(answer)