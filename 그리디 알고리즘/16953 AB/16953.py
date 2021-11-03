from sys import stdin as input
# input = open("./16953.txt")

start, end = map(int, input.readline().split())
list = [start]
result = 0
stop = False
while list:
    tmp_list = []
    if stop: break
    result += 1

    for num in list:
        if num == end:
            stop = True

        if (tmp := num*2) <= end:
            tmp_list.append(tmp)
        if (tmp := (num*10 + 1)) <= end:
            tmp_list.append(tmp)
    # print(tmp_list)
    list = tmp_list

if start == end:
    print(0)
elif not stop:
    print(-1)
else:
    print(result)
