import sys

sys.stdin = open("./11724.txt")

# 데이터 입력
node_count, line_count = map(int, sys.stdin.readline().split())
check_node_set = set(i for i in range(1, node_count+1))
linked_line_table = {i: set() for i in range(1, node_count+1)}
for _ in range(line_count):
    start, end = map(int, sys.stdin.readline().split())
    linked_line_table[start].add(end)
    linked_line_table[end].add(start)
    
result = 0
while check_node_set:
    node = check_node_set.pop()
    stack = linked_line_table[node].copy()
    result += 1
    
    while stack:
        check_node_set = check_node_set - stack
        node = stack.pop()
        check_node_set = check_node_set - linked_line_table[node]
        stack.update(linked_line_table[node].copy())

print(result)
print(linked_line_table)