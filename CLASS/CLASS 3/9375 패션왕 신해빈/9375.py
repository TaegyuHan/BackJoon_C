import sys
from functools import reduce
# 조합 문제
# 자신의 개수에서 NULL의 개수 1개를 추가해서 푸는 문제
# 수학적 지식이 요구

# sys.stdin = open('./9375.txt')

test_case = int(sys.stdin.readline())

# 테스트 개수
for _ in range(test_case): 
  result = 0
  tmp_dict = {} 

  # 옷 개수
  clothes_cont = int(sys.stdin.readline())
  if clothes_cont == 0:
    print(0)
    continue

  for _ in range(clothes_cont):

    _, category = sys.stdin.readline().split()

    if category not in tmp_dict.keys():
      tmp_dict[category] = 1
    else:
      tmp_dict[category] += 1

  print(reduce(lambda x, y: x * y, list(map(lambda x: x+1, tmp_dict.values())))-1)
