import sys

sys.stdin = open("./9237.txt")
input = sys.stdin.readline

n = int(input()) #묘목의 수 4
tree = sorted(map(int,input().split()),reverse=True) # 2 3 4 3

for i in range(len(tree)):
    tree[i] = tree[i] + i + 1 # 심는 일 수 + 자라는 일 수

print(max(tree) + 1) #이장님 다음날 오심