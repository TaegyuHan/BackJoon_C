import sys

# sys.stdin = open('./11727.txt')

N = int(sys.stdin.readline())

num_list = [1, 3]
for i in range(2, N):
    num_list.append(num_list[i - 2]*2 + num_list[i - 1])

print(num_list[N - 1]%10_007)