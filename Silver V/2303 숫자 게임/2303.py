import sys

# sys.stdin = open("./2303.txt")
member_count = int(sys.stdin.readline())
member_card_list = [list(map(int, sys.stdin.readline().split()))
                    for _ in range(member_count)]

def big_number(lst):
    max = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                tmp = (lst[i] + lst[k] + lst[j]) % 10
                if tmp > max:
                    max = tmp
    return max

max_tmp = 0
result = 0
for i, num in enumerate(map(big_number, member_card_list)):
    if num >= max_tmp:
        max_tmp = num
        result = i + 1

print(result)