import sys

# sys.stdin = open('./1003.txt')

for _ in range(int(sys.stdin.readline())):

    N = int(sys.stdin.readline())

    if N == 0:
        print("1 0")
        continue

    elif N == 1:
        print("0 1")
        continue
    
    else:
        back_count = (1, 0)
        current_count = (0, 1)
        for _ in range(1, N):
            temp_count = current_count
            current_count = tuple(sum(elem)
                                  for elem in zip(back_count, current_count))
            back_count = temp_count

        print(" ".join(map(str, current_count)))

