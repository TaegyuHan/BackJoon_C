from sys import stdin as input

input = open("./1700.txt")
N, K = map(int, input.readline().split())
table = [0 for _ in range(101)]
num_list = list(map(int, input.readline().split()))
power_socket = set()
result = 0

for num in num_list:
    table[num] += 1

num_list.reverse()
while num_list:
    num = num_list.pop()
    # print(num)