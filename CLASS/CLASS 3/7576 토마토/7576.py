from sys import stdin as input_data

input_data = open("./7576.txt")

width, height = \
    map(int, input_data.readline().split())

ripe_tomatoes_set = set()

for i in range(height):
    map(int, input_data.readline().split())
