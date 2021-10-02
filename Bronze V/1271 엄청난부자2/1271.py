import sys

# sys.stdin = open("./1271.txt")
a, b = map(int, sys.stdin.readline().split())
print(a//b, a%b)