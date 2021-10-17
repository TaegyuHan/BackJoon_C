import sys
# sys.stdin = open("./2693.txt")
for _ in range(int(sys.stdin.readline())):
    tmp_list = sorted(map(int, sys.stdin.readline().split()))
    print(tmp_list[-3])