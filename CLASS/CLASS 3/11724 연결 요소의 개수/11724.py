import sys

sys.stdin = open("./11724.txt")

# 데이터 입력
node_count, line_count = map(int, sys.stdin.readline().split())
check_node_set = set(i for i in range(1, node_count+1))
linked_line_table = {i:[] for i in range(1, node_count+1)}

for _ in range(line_count):
    start, end = map(int, sys.stdin.readline().split())
    linked_line_table[start].append(end)

print(check_node_set.pop())