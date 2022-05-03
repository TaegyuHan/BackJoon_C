"""Solution code for "BaekJoon ???. ???".

- Problem link: https://www.acmicpc.net/problem/???
"""

PUSH = 2

from sys import stdin as input
# input = open('./10845.txt')
INPUT_COUNT = int(input.readline())
queue = []

for _ in range(INPUT_COUNT):
    cmd = input.readline().strip().split()

    # 데이터 넣기
    if len(cmd) == PUSH:
        _, num = cmd
        queue.append(num)
        continue

    # 데이터 빼기
    cmd = cmd[0]
    if cmd in ("pop"):
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif cmd == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    # 큐 사이즈 확인
    elif cmd == "size":
        print(len(queue))

    # 큐 비어있는지 확인
    elif cmd == "empty":
        if not queue:
            print(1)
        else:
            print(0)

    # 큐에서 가장 뒤에 있는 정수를 출력
    elif cmd == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])