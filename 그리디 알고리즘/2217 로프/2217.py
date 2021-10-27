import sys

# sys.stdin = open("./2217.txt")
rope_cnt = int(sys.stdin.readline())
rope_list = [int(sys.stdin.readline()) for _ in range(rope_cnt)]
rope_list.sort(reverse=True)
max = 0
for i, num in enumerate(rope_list):
    if (tmp := num*(i + 1)) > max:
        max = tmp
print(max)