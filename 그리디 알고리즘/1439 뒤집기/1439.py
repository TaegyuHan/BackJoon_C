from sys import stdin as input
# input = open("./1439.txt")

S = input.readline().strip()
cnt = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        cnt += 1

print((cnt + 1) // 2)