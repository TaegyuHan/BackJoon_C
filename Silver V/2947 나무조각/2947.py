import sys

# sys.stdin = open("./2947.txt")
five_numbers = sys.stdin.readline().split()

j = 0
while j != 4:
    j = 0
    for i in range(1,len(five_numbers)):
        if five_numbers[i-1] > five_numbers[i]:
            tmp = five_numbers[i]
            five_numbers[i] = five_numbers[i-1]
            five_numbers[i - 1] = tmp
            print(" ".join(five_numbers))
        else:
            j += 1