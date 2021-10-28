from sys import stdin as input

# input = open("./1789.txt")

number = int(input.readline())

def max_number(num):
    n = 1
    while n*(n + 1)/2 <= num:
        n += 1
    print(n - 1)

max_number(number)