from sys import stdin as input
# input = open("./1912.txt")
N = int(input.readline())
nums = list(map(int, input.readline().split()))
DP = nums[:1] + [0 for _ in range(N-1)]
for i in range(1, N):
    DP[i] = max(DP[i-1] + nums[i], nums[i])
print(max(DP))