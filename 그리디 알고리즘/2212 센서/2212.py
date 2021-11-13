from sys import stdin as input

# input = open("./2212.txt")

senser_cnt = int(input.readline())
station_cnt = int(input.readline())
sensers = sorted(map(int, input.readline().split()))

if station_cnt > senser_cnt:
    print(0)
    exit()

senser_distance = []
for i in range(1, senser_cnt):
    senser_distance.append(sensers[i] - sensers[i - 1])
senser_distance.sort()

for _ in range(station_cnt - 1):
    senser_distance.pop()

print(sum(senser_distance))