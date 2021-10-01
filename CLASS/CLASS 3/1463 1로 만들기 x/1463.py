import sys

# sys.stdin = open('./1463.txt')
N = int(sys.stdin.readline())

#            0  1 숫자
num_list = [0, 0]

for num in range(2, N+1):
    min_num = num_list[num - 1] + 1 # 1빼는 경우

    if num % 3 == 0: # 3으로 나눠지는 경우   
        min_num = min(min_num, num_list[num//3] + 1)

    if num % 2 == 0:  # 2으로 나눠지는 경우
        min_num = min(min_num, num_list[num//2] + 1)

    num_list.append(min_num)

print(num_list[N])