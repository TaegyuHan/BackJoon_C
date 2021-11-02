from sys import stdin as input

# input = open("./1744.txt")

input_cnt = int(input.readline())
numbers_p = []
numbers_m = []
result = 0
last_num = []

for _ in range(input_cnt):
    num = int(input.readline())
    if num > 0:
        numbers_p.append(num)
    else:
        numbers_m.append(num)

numbers_p.sort(reverse=True)
numbers_m.sort()

# print(numbers_p)
def sum_numbers(number_list):
    sum = 0
    for i in range(0, len(number_list), 2):

        if len(number_list[i:i + 2]) == 1:
            last_num.append(number_list[i])
            break

        A, B = tuple(number_list[i:i + 2])
        sum += max(A * B, A + B)
    return sum

def last_num_sum(last_num):
    if len(last_num) == 0:
        return 0
    if len(last_num) == 1:
        return last_num[0]
    else:
        A, B = tuple(last_num)
    return max(A + B, A * B)

result += sum_numbers(numbers_p)
result += sum_numbers(numbers_m)
result += last_num_sum(last_num)
print(result)