from sys import stdin as input

# input = open("./2810.txt")
N = int(input.readline())

input_left_cup = True
next_chair = False
result = 0

for chair in input.readline():
    if next_chair:
        next_chair = False
        continue

    if chair == 'S':
        result += 1

    elif chair == 'L':
        next_chair = True
        if input_left_cup:
            result += 2
            input_left_cup = False
        else:
            result += 1

print(result)
