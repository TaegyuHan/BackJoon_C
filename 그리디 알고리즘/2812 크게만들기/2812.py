from sys import stdin as input

input = open("./2812.txt")
N, K = map(int, input.readline().split())
number_list = list(input.readline())

cnt = 0
while K > cnt:
    remove = {
        "index": 0,
        "num": number_list[0]
    }
    for i, num in enumerate(number_list[1:]):
        if remove["num"] > num:
            remove["num"] = num
            remove["index"] = i + 1
            continue

        if num > remove["num"]:
            break

    del number_list[remove["index"]]
    cnt += 1

print(''.join(number_list))