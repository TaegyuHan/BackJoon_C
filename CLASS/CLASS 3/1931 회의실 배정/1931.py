import sys

# sys.stdin = open("./1931.txt")

data_list = []
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    data_list.append((b, a))
data_list = sorted(data_list)

# 정렬된 데이터
last_end_time = -1
last_start_time = -1
meeting_cnt = 0

for data in data_list:
    end, start = data

    if (last_start_time <= end) and \
            (last_end_time <= start):
        meeting_cnt += 1
        last_end_time = end
        last_start_time = start

print(meeting_cnt)
