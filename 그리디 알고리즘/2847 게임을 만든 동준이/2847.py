from sys import stdin as input
# input = open("./2847.txt")
*point_list, max_point = [int(input.readline())
                          for _ in range(int(input.readline()))]

result = 0
for point in reversed(point_list):
    max_point -= 1
    if point > max_point:
        result += (point - max_point)
    elif point < max_point:
        max_point = point
print(result)