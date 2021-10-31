from sys import stdin as input

# input = open("./4796.txt")

i = 1
while tmp := tuple(map(int, input.readline().split())):
    if sum(tmp) == 0:
        break
    L, P, V = tmp
    sum_day = (V // P) * L
    remain_day = V - ((V // P) * P)
    if remain_day > L:
        sum_day += L
    else:
        sum_day += remain_day
    print(f"Case {i}: {sum_day}")
    i += 1