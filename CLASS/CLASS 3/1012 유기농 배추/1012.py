import sys

# 데이터 파일 읽기
# sys.stdin = open("./1012.txt")

# test 개수 확인
test_cnt = int(sys.stdin.readline())

for _ in range(test_cnt):

    # test 데이터
    width, height, cabbage_cnt = \
        map(int, sys.stdin.readline().split())

    position_list = set(tuple(map(int, sys.stdin.readline().split()))
                        for _ in range(cabbage_cnt))

    # 결과 저장
    earthworm = 0

    # 지렁이 1개 출격!
    while position_list:

        # 배추 저장 stack
        check_stack = [position_list.pop()]
        earthworm += 1

        # 배추 묶음 돌아다니기
        while check_stack:
            
            cabbage_position = check_stack.pop()
            x, y = cabbage_position[0], cabbage_position[1]

            up = (x, y + 1)
            down = (x, y - 1)
            left = (x + 1, y)
            right = (x - 1, y)
            tmp_set = {up, down, left, right}
            check_stack += list(tmp_set & position_list)

            # 확인한 배추 지우기
            for item in tmp_set:
                position_list.discard(item)

    print(earthworm)