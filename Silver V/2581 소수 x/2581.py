import sys

# sys.stdin = open('./2581.txt')

M = int(sys.stdin.readline())
N = int(sys.stdin.readline()) + 1
number_set = set(i for i in range(M, N))

sieve = [True] * N
sieve[1] = False
m = int(N ** 0.5)

for i in range(2, m + 1):
    if sieve[i] == True:              # i가 소수인 경우
        for j in range(i+i, N, i):  # i이후 i의 배수들을 False 판정
            sieve[j] = False

# 소수 목록 산출
for i in range(M, N):
    if sieve[i] != True:
        number_set.remove(i)

if len(number_set) != 0:
    print(sum(number_set))
    print(min(number_set))
else:
    print(-1)