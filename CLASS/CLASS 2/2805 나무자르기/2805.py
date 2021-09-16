import sys

sys.stdin = open('./2805.txt')


tree_cnt, M = map(int, sys.stdin.readline().split())
tree_size_list = list(map(int, sys.stdin.readline().split()))

high = max(tree_size_list)
low = 0

while(low < high-1):
    mid = (low + high) // 2

    # 2분탐색으로 얻은 값을 뺀것을
    # 더한 값
    tmp_sum = sum(map(lambda x: x - mid if (x - mid) > 0 else 0 , tree_size_list))

    if tmp_sum > M:
        low = mid
    else:
        high = mid
    
print(tmp_sum)
