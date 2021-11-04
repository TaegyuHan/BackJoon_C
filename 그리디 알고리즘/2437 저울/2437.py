from sys import stdin as input

# input = open("./2437.txt")
N = int(input.readline())
N_list = list(map(int, input.readline().split()))
N_list.sort()

num = 1
for i in range(N):
    # print(f"num < N_list[i] : {num} < {N_list[i]}")
    if num < N_list[i]:
        break
    num += N_list[i]
print(num)
