import sys

sys.stdin = open('./2447.txt')


# N = 3^k
# 1 ≤ k < 8
N = int(sys.stdin.readline())

empty_list = []

def recursion(r_start, c_start, size, empty):

    global empty_list

    size = size // 3

    if size == 0 and empty == 0:
        empty_list.append((r_start, c_start))

    if size == 0:
        return

    # 위 왼쪽
    recursion(r_start, c_start, size, empty)

    # 위 중앙
    recursion(r_start, c_start + size, size, empty)

    # 위 오른쪽
    recursion(r_start, c_start + size*2, size, empty)

    # 중앙 왼쪽
    recursion(r_start + size, c_start, size, empty)

    # 중앙 중앙
    recursion(r_start + size, c_start + size, size, 0)

    # 중앙 오른쪽
    recursion(r_start + size, c_start + size*2, size, empty)

    # 아래 왼쪽 
    recursion(r_start + size*2, c_start, size, empty)

    # 아래 중앙
    recursion(r_start + size*2, c_start + size, size, empty)

    # 아래 오른쪽
    recursion(r_start + size*2, c_start + size*2, size, empty)

recursion(0, 0, N, 1)

for i in range(N):
    for j in range(N):
        if (i, j) in empty_list:
            print(" ", end="")
        else:
            print("*", end="")
    print()
