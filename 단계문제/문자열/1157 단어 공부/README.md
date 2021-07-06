# 1157 단어 공부

URL : [https://www.acmicpc.net/problem/1157](https://www.acmicpc.net/problem/1157)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, result=0, TmpAlpha; //63은 ?
    char StringList[1000001], balpha;
    int j, sum=0, 
        count=0;

    scanf("%s", StringList);

    // 알파벳 소문자 for
    for (i=65; i<91; i++)
    {
        sum=0;
        for(j=0; StringList[j]!='\0'; j++)
        {   // 대소문자 대문자로 변경
            balpha = (StringList[j] > 90) ? StringList[j] - 32 : StringList[j];
            if (balpha==i)
            {
                sum++; // 현재 확인하는 알파벳이면 1 더하기
                TmpAlpha=balpha; // 현재 확인 문자 넣기
            }
        }
        if (sum==0) // 1개도 없으면 
            continue; 
        else if (sum == count) // 가장 큰 값이랑 같으면
            result=63; // ? 표 저장
        else if(sum > count) // 가장 큰 값보다 크면
        {
            result=TmpAlpha; // 알파벳 저장
            count=sum; // 합 저장
        }
    }
    printf("%c \n", result); // 마지막 저장 알파벳 출력
    return 0;
}
```

<br>

숏코딩

```c
int main() {
	char s[1000004]; // input 값
	int apb[26] = { 0, }; // 알파벳 배열 
	int i, max = 0; // for문처리 및 최대값
	char ans = ' '; // 물음표 값?

	scanf("%s", s); // input

	for (i = 0; s[i] != NULL; i++) {
		if (s[i] >= 'a' && s[i] <= 'z')
			s[i] += 'A' - 'a';
		apb[s[i] - 'A']++;
	}
	for (i = 0; i < 26; i++) {
		if (max < apb[i]) {
			max = apb[i];
			ans = i + 'A';
		}
		else if (max == apb[i])
			ans = '?';
	}
	printf("%c\n", ans);
	return 0;
}
```

```c
#include<stdio.h>
int main(){
	char c[1000001];
	int i,j,buf[28]={0},alp=0;

	gets(c);
	for (j=0;j<26;j++){
		for (i=0;c[i]!='\0';i++){
			if (c[i]==j+65) buf[j]++;
			else if (c[i]==j+97) buf[j]++;
		}
		if (buf[j]>alp) alp=buf[j];
	}
	for (i=0;i<26;i++){
		if (buf[i]==alp){
			buf[26]++;
			buf[27]=65+i;}
		if (buf[26]==2) {
			buf[27]=63;
			break;}
	}
	printf("%c",buf[27]);
}
```