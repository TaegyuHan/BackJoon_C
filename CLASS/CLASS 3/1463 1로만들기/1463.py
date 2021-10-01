import sys

sys.stdin = open('./1463.txt')

N = int(sys.stdin.readline())
count = 0
while N > 0:
    print(N)
    if N == 1:
        break

    elif N % 2 == 0:
        print("elif N % 2 == 0:")
        N = N // 2
        count += 1
        continue

    elif N % 3 == 0 and N < 13:
        print("elif N % 3 == 0:")
        N = N // 3
        count += 1
        continue

    elif (N - 1) % 2 == 0:
        print("elif (N - 1) % 2 == 0:")
        N -= 1
        N = N // 2
        count += 2
        continue

    elif (N - 1) % 3 == 0 and N < 13:
        print("elif (N - 1) % 3 == 0:")
        N -= 1
        N = N // 3
        count += 2
        continue

    else:
        print("else:")
        N -= 1
        count += 1
        continue

print(count)