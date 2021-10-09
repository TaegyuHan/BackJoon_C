from sys import stdin as input_data

# input_data = open("./15964.txt")
A, B = map(int, input_data.readline().split())
print((A + B)*(A - B))