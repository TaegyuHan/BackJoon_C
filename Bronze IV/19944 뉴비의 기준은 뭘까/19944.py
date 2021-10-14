from sys import stdin as input_data
# input_data = open('./19944.txt')
N, M = map(int, input_data.readline().split())
if M < 3:
    print("NEWBIE!")
elif 3 <= M and M <= N:
    print("OLDBIE!")
else:
    print("TLE!")
