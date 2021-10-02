import sys

# sys.stdin = open("./2606.txt")

N, row, col = map(int, sys.stdin.readline().split())
N = 2**N
result_count = 0

def recursive(row_index, col_index, size):
    
    # print(row_index, col_index, size)
    global result_count, check_stop
    global row, col
    # print(row, col)

    if size == 1:
        if row == row_index and col == col_index:
            return
        else:
            result_count += 1
            return

    size //= 2
    row_up = row_index - size
    row_down = row_index
    col_left = col_index - size
    col_right = col_index

    # 왼쪽 위
    if row_up >= row and col_left >= col:
        recursive(row_up, col_left, size)
        return
    else:
        result_count += size*size

    # 오른쪽 위
    if row_up >= row and col_right >= col:
        recursive(row_up, col_right, size)
        return
    else:
        result_count += size*size

    # 왼쪽 아래
    if row_down >= row and col_left >= col:
        recursive(row_down, col_left, size)
        return
    else:
        result_count += size*size
    
    # 오른쪽 아래
    if row_down >= row and col_right >= col:
        recursive(row_down, col_right, size)
        return
    else:
        result_count += size*size

recursive(N-1, N-1, N)
print(result_count)