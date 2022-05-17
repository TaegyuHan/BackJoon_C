import sys
input = sys.stdin.readline


str = input().rstrip()
st = []

for s in str:  # A-Z 까지 해당되는 알파벳이면 그대로 출력 해준다.
    if 0 <= ord(s)-ord('A') <= ord('Z'):
        print(s, end='')

    elif s == '(':
        st.append(s)

    elif s == ')':
        while st and st[-1] != '(':
            top = st.pop()
            print(top, end="")
        st.pop()  # 마지막 '(' 값 pop 처리

    # 스택의 top 값이 현재 순회중인 값 보다 우선 순위가 높거나 같다면 pop 해서 출력해준다
    elif s == '/' or s == '*':
        while st and (st[-1] == '/' or st[-1] == '*'):
            top = st.pop()
            print(top, end="")
        st.append(s)
    elif s == '+' or s == '-':
        while st and st[-1] != '(':
            top = st.pop()
            print(top, end="")
        st.append(s)

# 스택에 남은 값 처리
while st:
    top = st.pop()
    if top != '(':
        print(top, end="")