import sys

# sys.stdin = open("./1026.txt")
N = int(sys.stdin.readline())

A = sorted(map(int, sys.stdin.readline().split()))
B = sorted(map(int, sys.stdin.readline().split()), reverse=True)
sum = 0
for num1, num2 in zip(A, B):
    sum += num1*num2

print(sum)