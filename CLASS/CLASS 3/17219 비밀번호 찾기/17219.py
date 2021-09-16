import sys

# sys.stdin = open('./17219.txt')

site_count, find_pw_count = map(int, sys.stdin.readline().split())

url_dict = {}

# 데이터 넣기
for _ in range(site_count):
  url, pw = map(str, sys.stdin.readline().split())
  url_dict[url] = pw

# 비밀번호 풀기
for _ in range(find_pw_count):
  print(url_dict[sys.stdin.readline().strip('\n')])