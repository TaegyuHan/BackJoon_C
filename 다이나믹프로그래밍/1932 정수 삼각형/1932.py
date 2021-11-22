from sys import stdin as input
# input = open("./1932.txt")
N = int(input.readline())
number_list = []
for _ in range(N):
    number_list.append(list(map(int, input.readline().split())))

for i in range(N-1, 0, -1):
    for j in range(len(number_list[i-1])):
        number_list[i - 1][j] += max(number_list[i][j], number_list[i][j + 1])

print(number_list[0][0])