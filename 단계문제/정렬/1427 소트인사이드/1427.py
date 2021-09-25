import sys

# sys.stdin = open('./1427.txt')

N = sorted(map(str, sys.stdin.readline()))
for i in reversed(range(len(N))):
  print(N[i], end="")