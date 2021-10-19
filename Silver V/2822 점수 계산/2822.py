import sys

# sys.stdin = open("./2822.txt")
number_list = [int(sys.stdin.readline()) for _ in range(8)]

num_sum = 0
index_list = []
for num in sorted(number_list)[3:]:
    num_sum += num
    index_list.append(str(number_list.index(num) + 1))

print(num_sum)
print(" ".join(sorted(index_list)))