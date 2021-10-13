import sys
# sys.stdin = open("./19698.txt")
N, W, H, L = map(int, sys.stdin.readline().split())
if N > (W//L)*(H//L):
    print((W//L)*(H//L))
else:
    print(N)