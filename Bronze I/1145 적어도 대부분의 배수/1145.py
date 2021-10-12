from sys import stdin as input_data
# input_data = open("./1145.txt")

result = 0
number_map = list(map(int, input_data.readline().split()))
loop = True
while loop:
    division_count = 0
    result += 1
    for num in number_map:
        if result % num == 0:
            division_count += 1
        if division_count == 3:
            loop = False
            break
print(result)