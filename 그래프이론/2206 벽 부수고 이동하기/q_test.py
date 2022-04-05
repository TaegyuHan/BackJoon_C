from collections import deque
q = deque([[100, 100, 100]])

while q:
    print(q.popleft())
    print(q.append([100,100,100]))