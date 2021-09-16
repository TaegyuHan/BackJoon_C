import sys

# sys.stdin = open('./2805.txt')

tree_cnt, M = map(int, sys.stdin.readline().split())
tree_size_list = list(map(int, sys.stdin.readline().split()))

end = max(tree_size_list)
start = 0
result = 0

while (start <= end):
    mid = (start + end) // 2

    # 2분탐색으로 얻은 값을 뺀것을
    # 더한 값
    tmp_sum = sum(map(lambda x: x - mid if (x - mid) > 0 else 0 , tree_size_list))

    if tmp_sum >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)