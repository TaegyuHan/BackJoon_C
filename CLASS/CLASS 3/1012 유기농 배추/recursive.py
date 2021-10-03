import sys

# 데이터 파일 읽기
sys.stdin = open("./1012.txt")

# 데이터 삽입
test_cnt = int(sys.stdin.readline())

def remove_adjacent_cabbage(position_list, cabbage_position):
    x, y = cabbage_position[0], cabbage_position[1]

    up = (x, y + 1)
    down = (x, y - 1)
    left = (x + 1, y)
    right = (x - 1, y)

    # 상
    if up in position_list:
        position_list.remove(up)
        remove_adjacent_cabbage(position_list, up)
    # 하
    if down in position_list:
        position_list.remove(down)
        remove_adjacent_cabbage(position_list, down)
    # 좌
    if left in position_list:
        position_list.remove(left)
        remove_adjacent_cabbage(position_list, left)
    # 우
    if right in position_list:
        position_list.remove(right)
        remove_adjacent_cabbage(position_list, right)
        

for _ in range(test_cnt):

    width, height, cabbage_cnt = \
        map(int, sys.stdin.readline().split())

    position_list = set(tuple(map(int, sys.stdin.readline().split()))
                        for _ in range(cabbage_cnt))

    earthworm = 0

    while position_list:
        earthworm += 1
        remove_adjacent_cabbage(position_list, position_list.pop())

    print(earthworm)