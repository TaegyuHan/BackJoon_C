from sys import stdin as input

# input = open("./1339.txt")

string_cnt = int(input.readline())
table = {}
number = 9
result = 0
for _ in range(string_cnt):
    tmp_alpha = input.readline().rstrip()
    for i , alpha in enumerate(reversed(tmp_alpha)):
        tmp_num = 1*pow(10, i)
        if alpha not in table:
            table[alpha] = tmp_num
        else:
            table[alpha] += tmp_num

for key, val in sorted(table.items(), key=lambda x: x[1], reverse=True):
    result += val*number
    number -= 1

print(result)
