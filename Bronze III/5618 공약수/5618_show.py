from sys import stdin as input

input = open('./5618.txt')

def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)

n = int(input.readline())
s = list(map(int, input.readline().split()))

print(gcd(s[1], s[-1]))
print(gcd(s[0], gcd(s[1], s[-1])))

g = gcd(s[0], gcd(s[1], s[-1]))
for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)