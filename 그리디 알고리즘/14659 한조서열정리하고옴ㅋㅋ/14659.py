from sys import stdin as input
# input = open("./14659.txt")
N = int(input.readline())
mountains = list(map(int, input.readline().split()))

tmp_mountain_height = 0
tmp_kill_cnt = 0
result = 0
for mountain_height in mountains:
    if mountain_height > tmp_mountain_height:
        tmp_mountain_height = mountain_height
        tmp_kill_cnt = 0
        continue

    tmp_kill_cnt += 1
    result = max(result, tmp_kill_cnt)

print(result)