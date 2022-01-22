import sys
# sys.stdin = open("./9020.txt")
# Test 파일 불러오기
# ------------------------------- #

# 9020: 골드바흐의 추측
# ------------------------------- #
# 기존 코드
"""
def prime_list(n): # 에라토스테네스의 체
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for x in range(i + i, n, i):
                sieve[x] = False
    return [i for i in range(2, n) if sieve[i] == True]
"""
# 변경 코드
# 에라토스테네스의 체
MAX = 10_001
sieve = [True] * MAX
for i in range(2, MAX):
    if sieve[i] == True:
        for x in range(i*2, MAX, i):
            sieve[x] = False
# ------------------------------- #

# ------------------------------- #
# 기존코드
"""
T = int(input())
gold_list = []
for j in range(T):
    n = int(input())
    gold =[]
    primes = prime_list(n) # < 1줄 들어올 때마다 에라토스테네스의 체 실행 (느린부분)
    for k in primes:
        if n - k in primes:
            if k <= n - k: # < 여기서 정답을 찾아야 함
                gold += [[k, n - k]]
    gold_list += [gold[-1]]
    gold_list = gold_list + [gold[-1]]
    
for a, b in gold_list: < 정답을 찾기 위해서 리스트로 저장할 필요 없음 (느린부분)
    print(a, b)
"""

# 변경 코드
TEST_CASE = int(input())
for j in range(TEST_CASE):
    n = int(input()) # 데이터 받기

    number_distance = MAX # 정답 찾기위한 숫자 2개 거리 비교 저장
    answer = (0, 0) # 정답 저장 공간

    for i in range(1, (n//2) + 1):
        # <  (n//2) + 1 # 10이 들어온다고 하면 5까지 비교해야함
        # 10 까지 갈필요 없음  < (시간 단축)
        if sieve[i] == True and sieve[n - i] == True: # 둘다 소수 인지 확인

            # tmp := abs((n - i) - i) < 의미 : abs((n - i) - i)값 tmp에 저장
            if number_distance > (tmp := abs((n - i) - i)):
                # 정답 찾는  if 문 2개의 수 거리 비교
                answer = (n - i, i) # 정답 저장
                number_distance = tmp

    answer = sorted(answer) # 낮은 수가 앞으로 정렬
    print(answer[0], answer[1]) # 정답 출력
# ------------------------------- #