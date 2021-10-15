import sys

# sys.stdin = open("./1236.txt")
row, col  = map(int, sys.stdin.readline().split())

check_row_list = [False for _ in range(col)]
check_col_list = [False for _ in range(row)]

# print(check_row,check_col)

for i in range(row):
    for j, state in enumerate(sys.stdin.readline().rstrip()):
        if state == 'X':
            check_row_list[j] = True
            check_col_list[i] = True
row_empty = 0
col_empty = 0

for i, state in enumerate(check_row_list):
    if state == False:
        row_empty += 1
        
for i, state in enumerate(check_col_list):
    if state == False:
        col_empty += 1

if row_empty == col_empty:
    print(row_empty)
elif row_empty > col_empty:
    print((row_empty - col_empty) + col_empty)
else:
    print((col_empty - row_empty) + row_empty)