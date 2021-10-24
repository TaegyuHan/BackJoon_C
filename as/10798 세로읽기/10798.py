import sys

# sys.stdin = open("./10798.txt")
table = {}
for _ in range(5):
    for j ,_str in enumerate(sys.stdin.readline().rstrip()):
        if j not in table:
            table[j] = []
        table[j].append(_str)

for val in table.values():
    print("".join(val), end="")