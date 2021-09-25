import sys

# sys.stdin = open('./1427.txt')

N = sorted(map(str, sys.stdin.readline()), reverse=True)
for i in range(len(N)):
  print(N[i], end="")