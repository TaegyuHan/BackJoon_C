import sys

# sys.stdin = open("./10808.txt")

text = sys.stdin.readline().strip()
alpabet_list = [0 for i in range(26)]

for _str in text:
    alpabet_list[ord(_str) - 97] += 1

print(" ".join(map(str, alpabet_list)))