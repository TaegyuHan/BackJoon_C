n=int(input());
print(min(n,n-input().count('L')//2+1))