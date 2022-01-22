# 9020: 골드바흐의 추측
# ------------------------------- #
def prime_list(n): # 에라토스테네스의 체
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for x in range(i + i, n, i):
                sieve[x] = False
    return [i for i in range(2, n) if sieve[i] == True]


T = int(input())
gold_list = [] # 나중에 정답을 한 번에 출력하기 위한 리스트
for j in range(T): # 테스트 케이스
    n = int(input())
    gold =[]
    primes = prime_list(n)
    for k in primes:
        if n - k in primes:
            if k <= n - k:
                gold += [[k, n - k]]
    gold_list += [gold[-1]]
for a, b in gold_list:
    print(a, b)