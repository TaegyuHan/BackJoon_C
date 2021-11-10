from sys import stdin as input

# input = open("./2812.txt")
N, K = map(int, input.readline().split())
number_list = list(input.readline())
del_cnt, result = K, []

for num in number_list:
    # 값이 있거나 다 지운 경우
    while del_cnt > 0 and result:
        if result[-1] < num:
            result.pop()
            del_cnt -= 1
        else:
            break
    result.append(num)
    
print(''.join(result[:N-K]))