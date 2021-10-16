import sys

# sys.stdin = open("./1476.txt")

earth, sun, moon = map(int, sys.stdin.readline().split())

t_earth = 1
t_sun = 1
t_moon = 1

result = 1
while True:

    if t_earth % 16 == 0:
        t_earth = 1

    if t_sun % 29 == 0:
        t_sun = 1

    if t_moon % 20 == 0:
        t_moon = 1

    if t_earth == earth and \
        t_sun == sun and \
        t_moon == moon:
          break

    t_earth += 1
    t_sun += 1
    t_moon += 1
    result += 1

print(result)