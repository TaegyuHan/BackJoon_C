from sys import stdin as input

# input = open("./1449.txt")
N, tape_lenght = map(int, input.readline().split())
trouble_list = sorted(map(int, input.readline().split()))

result = 0
trouble_start = 0
for trouble in trouble_list:
    if trouble_start < trouble:
        trouble_start = trouble - 0.5 + tape_lenght
        result += 1
print(result)




