import sys
from collections import deque


def make_graph(edges):
    graph = {n + 1: [] for n in range(N)}

    for frm, to, cost in edges:
        graph[frm].append([to, cost])
        graph[to].append([frm, cost])

    return graph


def bfs(start, goal):
    q = deque()
    visit = [0] * (N + 1)

    q.append([start, 0])
    visit[start] = 1

    while q:
        here, acc_cost = q.popleft()
        if here == goal:
            return acc_cost

        for there, cost in graph[here]:
            if not visit[there]:
                visit[there] = 1
                q.append([there, cost + acc_cost])


def solution(frm, to):
    return bfs(frm, to)


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
    pairs = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    graph = make_graph(edges)

    for frm, to in pairs:
        answer = solution(frm, to)
        print(answer)