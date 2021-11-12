from sys import stdin as input

# input = open("./11497.txt")
test_cnt = int(input.readline())

for _ in range(test_cnt):
    cnt = int(input.readline())
    log_lengths = sorted(map(int, input.readline().split()))
    result = 0
    for i in range(2, cnt):
        result = max(result, abs(log_lengths[i] - log_lengths[i - 2]))
    print(result)