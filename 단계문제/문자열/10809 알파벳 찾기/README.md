# 10809 알파벳 찾기

URL : [https://www.acmicpc.net/problem/10809](https://www.acmicpc.net/problem/10809)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char StringArray[101]; // 입력받을 수를 저장할 배열
    char i, j=0;
    char len = 0;

    scanf("%s", StringArray);

    // 문자열 길이 구하기
    for (i=0; StringArray[i] != '\0'; i++) len++;

    for (i=0; i<26; i++)
    {   
        j=0;
        while(StringArray[j]!=0)
        {
            if((i+97)==StringArray[j])
            {
                printf("%d ", j);
                break;
            }
            j++;
        }
        if(len==j)
            printf("%d ", -1);
    }
    return 0;
}
```

숏 코딩

```c
#include<stdio.h>

int main(){

    char a[101],i,ans[26]={0,};
    scanf("%s",a);
    while(a[i]!=0){
        if(ans[a[i]-'a']==0) ans[a[i]-'a']=i+1;
        i++;
    }
    for(i=0;i<26;i++){
        printf("%d ",ans[i]-1);
    }
}
```

```c
#include <stdio.h>

char str[101];
int i, alpha[26];
 
int main(){
	scanf("%s", str);
	for(i=0;str[i]!=0;i++){
		int temp = (int) str[i] - 'a';
		if(alpha[temp]==0)alpha[temp] = i+1;
	}
	for(i=0;i<26;i++){
		printf("%d ", alpha[i]-1);
	}
}
```