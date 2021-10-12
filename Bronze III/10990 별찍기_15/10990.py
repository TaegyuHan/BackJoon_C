from sys import stdin as input_data

# input_data = open("./10990.txt")
N = int(input_data.readline())

star = '*'
i = N - 1
k = 1
for j in range(N):
    if j == 0:
        print(f"{(' '*i)}{star}")
    else:
        print(f"{(' '*i)}{star}{' '*k}{star}")
        k += 2
    i -= 1