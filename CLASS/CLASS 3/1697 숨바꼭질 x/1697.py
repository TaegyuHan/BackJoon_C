# https://www.acmicpc.net/problem/1697
from sys import stdin as input_data

# input_data = open("./1697.txt")
me, brother = map(int, input_data.readline().split())

check_list = [True for _ in range(100_001)]

queue_list = [me]
meet = True
result = -1

while meet:
    tmp = []
    result += 1
    for me in queue_list:
        if me == brother:
            meet = False
            break

        if check_list[me]:
            check_list[me] = False

            for next in [me - 1, me + 1, me*2]:
                if 0 <= next <= 100_000:
                    if check_list[next]:
                        tmp.append(next)

    queue_list = tmp.copy()

print(result)