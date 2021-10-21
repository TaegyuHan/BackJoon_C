import sys
# sys.stdin = open("./2744.txt")

change = lambda x: x.lower() if x.isupper() else x.upper()
print("".join(map(change, sys.stdin.readline())))