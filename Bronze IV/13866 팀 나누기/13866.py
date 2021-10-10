from sys import stdin as input_data

# input_data = open("./13866.txt")
A, B, C, D = map(int, input_data.readline().split())
print(abs((D + A) - (B + C)))