import sys

_, _, *i = open("./2606.txt")

print(n := [-1, 1]+[0]*99)

for _ in (n := [-1, 1]+[0]*99):
  for l in i:
    a, b = map(int, l.split())
    n[b] = n[a] = n[a] | n[b]
print(sum(n))
