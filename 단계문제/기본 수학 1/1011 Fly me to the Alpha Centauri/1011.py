import sys
##
sys.stdin = open('./1011.txt')

test_coumt = int(sys.stdin.readline())

i = 1
tmp = 0
while tmp < 2**31:
    tmp = sum(range(1, i))*2
    print(sum(range(1, i))*2)
    i += 1

for _ in range(test_coumt):
    x, y = map(int, sys.stdin.readline().split())
    print(y - x)