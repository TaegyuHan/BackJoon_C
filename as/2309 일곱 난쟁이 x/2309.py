import sys

sys.stdin = open("./2309.txt")

mas_list = sorted([int(sys.stdin.readline()) for _ in range(9)])
sum = sum(mas_list)

_break = False

for i in range(len(mas_list)):
    for j in range(i+1, len(mas_list)):
        if (sum - mas_list[i] - mas_list[j]) == 100:
            rm_tmp1 = mas_list[i]
            rm_tmp2 = mas_list[j]
            mas_list.remove(rm_tmp1)
            mas_list.remove(rm_tmp2)
            _break = True
            break
    if _break:
        break

for i in mas_list:
    print(i)
