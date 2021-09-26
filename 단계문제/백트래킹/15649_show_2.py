import itertools

N, M = map(int, input().split())
for p in itertools.permutations(range(1, N+1), M):
    print(' '.join(map(str, p)))