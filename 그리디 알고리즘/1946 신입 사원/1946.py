from sys import stdin as input

# input = open("./1946.txt")
test_cnt = int(input.readline())

for _ in range(test_cnt):
    meeting = int(input.readline())
    test_list = []

    for _ in range(meeting):
        test_data = tuple(map(int, input.readline().split()))
        test_list.append(test_data)

    test_list.sort()

    recruitment = 1
    max_tmp = test_list[0][1]
    for i, (_, test) in enumerate(test_list):
        if max_tmp > test:
            recruitment += 1
            max_tmp = test

    print(recruitment)

