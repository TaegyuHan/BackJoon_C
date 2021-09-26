import sys

sys.stdin = open('./1463.txt')

N = int(sys.stdin.readline())
restul_count = 0

def find_count(num):

    if num == 1: return

    global restul_count
    restul_count += 1

    if num % 2 == 0 and (num-1) % 3 == 0:
    elif num % 3 == 0:
    elif num % 2 == 0:

    return find_count(num - 1) + find_count(num - 2) + find_count(num - 3)

for _ in range(N):
  tmp = int(sys.stdin.readline())
  print(find_count(tmp))
