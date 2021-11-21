from sys import stdin as input
# input = open("./11053.txt")
N = int(input.readline())
NB = list(map(int, input.readline().split()))
DP = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if NB[i] > NB[j] and DP[i] < DP[j]:
            DP[i] = DP[j]
    DP[i] += 1
print(max(DP))