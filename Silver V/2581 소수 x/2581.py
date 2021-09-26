import sys

sys.stdin = open('./2581.txt')

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())


def prime_list(start, end):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)

    sieve = [True] * end

    # n의 최대 약수가 sqrt(end) 이하이므로 i=sqrt(end)까지 검사
    m = int(end ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:              # i가 소수인 경우
            for j in range(i+i, end, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(start, end) if sieve[i] == True]


list = prime_list(M, N)

if len(list) > 0:
    print(sum(list))
    print(min(list))
else:
    print(-1)