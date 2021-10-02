import sys

sys.stdin = open("./2606.txt")

def DFS(s):
    visit[s] = True
    S.append(s)

    for w in G[s]:
        if not visit[w]:
            DFS(w)
            

N = int(input())
M = int(input())

G = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
S = []
visit = [False] * (N+1)


DFS(1)
print(len(S)-1)