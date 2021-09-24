import sys

# sys.stdin = open('./2750.txt')

N = int(sys.stdin.readline())
int_list = [int(sys.stdin.readline()) for _ in range(N)]
int_list.sort()
for num in int_list:
    print(num)