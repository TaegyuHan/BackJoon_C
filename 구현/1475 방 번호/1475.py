import sys

# sys.stdin = open("./1475.txt")

table_list = []

for i in range(10):
    table_list.append(0)

for _str in sys.stdin.readline().rstrip():
  table_list[int(_str)] += 1

max = 0
for i in range(10):
    if i in [6, 9]:
        continue
    
    if table_list[i] > max:
        max = table_list[i]

if max < (tmp := ((table_list[6] + table_list[9]) // 2) +
          ((table_list[6] + table_list[9]) % 2)):
          max = tmp

print(max)