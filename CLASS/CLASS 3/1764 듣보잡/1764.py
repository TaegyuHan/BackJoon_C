import sys

# sys.stdin = open('./1764.txt')

N_count, M_count = \
  map(int, sys.stdin.readline().split())

N_set = set([sys.stdin.readline().strip() for _ in range(N_count)])
M_set = set([sys.stdin.readline().strip() for _ in range(M_count)])

print(len(N_set & M_set))
for man in sorted((N_set & M_set)):
  print(man)