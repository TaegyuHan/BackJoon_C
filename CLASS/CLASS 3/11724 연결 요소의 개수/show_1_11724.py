import sys
n, m = map(int,input().split())
g = {}
f = lambda x: f(g[x]) if x in g else x
for s in sys.stdin:
  u, v = sorted(map(f, s.split()))
  if u != v:
      n -= 1
      g[v]=u
      
print(n)