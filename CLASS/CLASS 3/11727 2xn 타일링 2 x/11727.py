import sys
sys.setrecursionlimit(5000)

sys.stdin = open('./11727.txt')

N = int(sys.stdin.readline())

def find_count(num):

    if num == 1: return 1
    elif num == 2: return 1

    return find_count(num - 1) + find_count(num - 2)

print(find_count(N%10007))