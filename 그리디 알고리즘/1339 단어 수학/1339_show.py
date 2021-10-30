from sys import stdin as input

input = open("./1339.txt")

d=[0]*99
for i in[1]*int(input.readline()):
 for c in input.readline()[::-1]:d[ord(c)]-=i;i*=10
print(sum(b*a for a,b in zip(sorted(d),range(-9,0))))