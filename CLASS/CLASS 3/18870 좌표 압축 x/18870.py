import sys

sys.stdin = open('./18870.txt')

# 데이터 받기
input_count = int(sys.stdin.readline())
X_list = sys.stdin.readline().split()

number_count = dict((l, X_list.count(l)) for l in set(X_list))

sum = 0
for key in sorted(map(int, number_count.keys())):
  number_count[str(key)] = (number_count[str(key)], sum)
  sum += 1

for key in X_list:
  print(number_count[key][1], end=" ")