from sys import stdin as input

input = open("./1339.txt")

def alpha_to_int(alpha):
    return ord(alpha) - 65

def alpha_to_count(alpha):
    global alpha_count
    return alpha_count[alpha_to_int(alpha)]

def string_to_int(_str):
    return alpha_number[alpha_to_int(_str)]

string_cnt = int(input.readline())
alpha_count = [0 for _ in range(10)]
alpha_number = [0 for i in range(10)]
used_alpha = set()
alpha_table = {}
nine_to_zero = 9
number_list = []
result = 0

for _ in range(string_cnt):
    tmp_alpha = input.readline().rstrip()
    number_list.append(tmp_alpha)
    for i, at_index in enumerate(range(len(tmp_alpha) - 1, -1, -1)):
        alpha = tmp_alpha[i]
        if at_index not in alpha_table:
            alpha_table[at_index] = []

        alpha_table[at_index].append(alpha)
        tmp_index = alpha_to_int(alpha)
        alpha_count[tmp_index] += 1

for key in sorted(alpha_table.keys(), reverse=True):
    tmp_key = alpha_table[key]
    tmp_cnt = list(map(alpha_to_count, alpha_table[key]))
    print(list(zip(tmp_key, tmp_cnt)))
    numbers = sorted(zip(tmp_key, tmp_cnt),
                     key=lambda x : (x[0], x[1]))

    while numbers:
        ap, cnt = numbers.pop()
        if ap in used_alpha:
            continue

        used_alpha.add(ap)
        alpha_number[alpha_to_int(ap)] = str(nine_to_zero)
        nine_to_zero -= 1

for string in number_list:
    result += int("".join(map(string_to_int, string)))

print(alpha_number)
print(result)