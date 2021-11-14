from sys import stdin as input
# input = open("./15904.txt")

check_alpha = ['U', 'C', 'P', 'C']
words = input.readline()
cnt = 0

for alpha in check_alpha:
    if alpha in words:
        words = words[words.index(alpha) + 1:]
        cnt += 1
    else:
        print('I hate UCPC')
        break

if cnt == 4:
    print('I love UCPC')