from sys import stdin as input
# input = open("./2720.txt")
cash = [25, 10, 5, 1]
for _ in range(int(input.readline())):
    money = int(input.readline())
    index = 0
    result = ['0', '0', '0', '0']
    while money:
        cnt = money // cash[index]
        money -= cnt*cash[index]
        result[index] = str(cnt)
        index += 1
    print(" ".join(result))