n=int(input())
d=list(map(int,input().split()))
p=list(map(int,input().split()))
s=0
k=p[0]
for i in range(n-1):
    if p[i]<k:
        k=p[i]
    s+=k*d[i]
print(s)