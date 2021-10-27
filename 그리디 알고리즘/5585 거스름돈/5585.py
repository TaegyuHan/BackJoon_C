import sys

# sys.stdin = open("./5585.txt")

change = [500, 100, 50, 10, 5, 1]
money = 1_000
give_change = money - int(sys.stdin.readline())
result = 0
while give_change:
    for coin in change:
        if (give_change - coin) >= 0:
            give_change -= coin
            result += 1
            break
print(result)