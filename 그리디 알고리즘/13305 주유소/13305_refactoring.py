from sys import stdin as input

# input = open("./13305.txt")

city_count = int(input.readline())
road_length = list(map(int, input.readline().split()))
city_price = list(map(int, input.readline().split()))

sum_price = 0
tmp_price = city_price[0]
for i, (length, price) in enumerate(zip(road_length, city_price)):

    if tmp_price > price:
        tmp_price = price

    sum_price += tmp_price*length

print(sum_price)