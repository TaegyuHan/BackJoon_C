import sys
# sys.stdin = open("./1541.txt")
minus_div = sys.stdin.readline().split('-')
num_list = []
for num in minus_div:
    tmp_sum = sum(map(int, num.split("+")))
    num_list.append(tmp_sum)

plus_num, *minus_num = num_list
print(plus_num - sum(minus_num))