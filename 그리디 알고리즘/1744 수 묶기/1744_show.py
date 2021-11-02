n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse = True)
b = 0
while len(a) >= 2:
    if a[-1]<=0 and a[-2]<=0:
        b += a.pop()*a.pop()
    else:
        break
a.sort()
while len(a) >= 2:
    if a[-1]>=2 and a[-2]>=2:
        b += a.pop()*a.pop()
    else:
        break
print(sum(a)+b)