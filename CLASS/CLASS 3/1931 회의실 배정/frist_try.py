import sys

# sys.stdin = open("./1931.txt")

meeting_cnt = int(sys.stdin.readline())
table = {}

for _ in range(meeting_cnt):
    start_time, end_time = map(int, sys.stdin.readline().split())
    time_term = end_time - start_time

    if start_time in table:
        if table[start_time]["min_time"] > time_term:
            table[start_time]["min_time"] = time_term
            table[start_time]["time_list"] = (start_time, end_time)
    else:
        table[start_time] = {"min_time" : time_term,
                             "time_list" : (start_time, end_time)}

key_set = set(table.keys())
result_cnt = 0
key_sort_list = list(sorted(key_set))
key_sort_index = 0
maximum_time = table[key_sort_list[-1]]["time_list"][1]
# print(table)
# 처음 회의 시작부터
# 마지막 회의 시작까지 확인
for key in key_sort_list:
    key_sort_index += 1
    current_time = key
    tmp_cont = 0
    # print(f"key : {key}")

    # 첫 회의 시작 고정
    # 뒤의 시간 가장 많이 넣을 수 있는 조건
    while current_time <= maximum_time:
        
        tmp_cont += 1
        current_time = table[current_time]["time_list"][1] + 1

        # 회의 찾고 다음 가장 빠른 회의
        for nk in range(key_sort_index, len(key_sort_list)):
            if key_sort_list[nk] >= current_time:
                current_time = key_sort_list[nk]
                break

        if current_time not in key_set:
            break
    
    # 다음 key가 없으면 종료
    if tmp_cont > result_cnt:
        result_cnt = tmp_cont

print(result_cnt)