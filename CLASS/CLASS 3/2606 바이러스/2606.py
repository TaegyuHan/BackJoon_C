import sys

# sys.stdin = open("./2606.txt")

computer_cnt = int(sys.stdin.readline())

connection_matrix = \
    [[False]*(computer_cnt) for _ in range(computer_cnt)]

link_cnt = int(sys.stdin.readline())

for _ in range(link_cnt):
    start, end = \
      map(lambda x: int(x)-1, sys.stdin.readline().split())
    connection_matrix[start][end] = True
    connection_matrix[end][start] = True

check_computer = 0
check_set = set()
stack_list = []
infected_computer_cnt = 0

while True:

    # set에 있나 확인
    if check_computer in check_set:
        if len(stack_list) == 0:
            infected_computer_cnt -= 1
            break

        check_computer = stack_list.pop()
        continue

    # 연결 확인 후 스택에 넣기
    for i, val in enumerate(connection_matrix[check_computer]):
        if val and (i not in check_set):
            stack_list.append(i)

    if len(stack_list) == 0:
        break

    check_set.add(check_computer)
    check_computer = stack_list.pop()
    infected_computer_cnt += 1

print(infected_computer_cnt)