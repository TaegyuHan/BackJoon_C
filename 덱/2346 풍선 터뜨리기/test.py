n = int(input())
inp = list(map(int, input().split()))
index = 0
in_list = []
result = []
for i in range(1,n+1):
    in_list.append(i)
num = inp.pop(index)  # 풍선 안에 적혀있는 숫자
result.append(in_list.pop(index))
while inp:
    if num < 0:
        index = (index + num) % len(inp)
    else:
        index = (index + num -1) % len(inp)
    num = inp.pop(index)
    result.append(in_list.pop(index))

for i in result:
    print(i, end=" ")