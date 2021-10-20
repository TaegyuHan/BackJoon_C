import sys

# sys.stdin = open("./1100.txt")
result = 0
white_check = 1
for _ in range(8):
    for i, state in enumerate(sys.stdin.readline().strip()):
        if white_check == 1:
            if i%2 == 0 and state == 'F':
                result += 1
        else:
            if i % 2 != 0 and state == 'F':
                result += 1

    if white_check == 1:
        white_check = -1
    else:
        white_check = 1

print(result)