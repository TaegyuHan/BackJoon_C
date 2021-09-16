import sys

# sys.stdin = open('./9095.txt')

N = int(sys.stdin.readline())

def find_count(num):
  
    if num == 1: return 1
    elif num == 2: return 2
    elif num == 3: return 4

    return find_count(num - 1) + find_count(num - 2) + find_count(num - 3)

for _ in range(N):
  tmp = int(sys.stdin.readline())
  print(find_count(tmp))