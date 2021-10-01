import sys

# sys.stdin = open('./18870.txt')

# 데이터 받기
input_count = int(sys.stdin.readline())
X_list = list(map(int, sys.stdin.readline().split()))

# 데이터 key 정렬
unique_value = sorted(set(X_list))

# 테이블 만들기
table = dict((unique_value[index], index)
             for index in range(len(unique_value)))

# 출력
print(' '.join(map(lambda x: str(table[x]), X_list)))