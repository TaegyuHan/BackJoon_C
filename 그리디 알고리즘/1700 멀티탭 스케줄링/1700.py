from sys import stdin as input

# input = open("./1700.txt")
N, K = map(int, input.readline().split())
use_it_cnt = [0 for _ in range(K + 1)]
item_number = [int(i) for i in input.readline().rstrip().split()]

count = 0
using_multitab = 0
use = []

for index, item in enumerate(item_number):

    # 멀티탭이 비어있고, 사용중이 아닐때
    if using_multitab < N and item not in use:
        using_multitab += 1
        use.append(item) # 멀티탭 사용
        continue

    # 멀티탭 이미 사용중
    if item in use:
        continue

    # 가장 마지막에 사용할 아이템 제거
    remove_value = None
    remove_index = 0

    # 사용중인 멀티탭에서 확인
    for using_item in use:
        # 앞으로 사용 안하는 아이템 제거
        if using_item not in item_number[index:]:
            remove_value = using_item
            break

        # 가장 늦게 사용하는 아이템 찾기
        for g_index, going_2_use in enumerate(item_number[index:]):
            if going_2_use == using_item:
                if remove_index < g_index + index:
                    remove_index = g_index + index
                    remove_value = going_2_use
                break

    # 제거
    if remove_value:
        use.remove(remove_value)
    else:
        use.pop()
    count += 1
    use.append(item)

print(count)