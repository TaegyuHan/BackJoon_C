from sys import stdin as input

# input = open("./13305.txt")

city_count = int(input.readline())
road_length = list(map(int, input.readline().split()))
city_price = list(map(int, input.readline().split()))

for i, (length, price) in enumerate(zip(road_length, city_price)):

    if i == 0:
        sum_price = 0
        tmp_price = price
        tmp_length = length
        continue

    if tmp_price > price:
        sum_price += tmp_length*tmp_price
        tmp_length = length
        tmp_price = price
    else:
        tmp_length += length

    if i == len(road_length) - 1:
        sum_price += tmp_length * tmp_price

print(sum_price)