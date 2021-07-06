# 1152 단어의 개수

URL : [https://www.acmicpc.net/problem/1152](https://www.acmicpc.net/problem/1152)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char StrList[1000001], tmp=0;
    unsigned int i, result=0;

    // %[^\n]s > \n 값이 들어오기전까지 문자열 받기
    scanf("%[^\n]s", StrList);

    for(i=0; StrList[i]!='\0'; i++)
    {
        if (tmp==0 && StrList[i]!=32) // 단어 시작 ASCII 띄어쓰기 32번
        {
            tmp=1; 
            result+=1; 
        }
        else if (StrList[i]==32) // 띄어쓰기 부분
        {
            tmp=0; 
        }
    }

    printf("%d", result);

    return 0;
}
```

<br>

숏 코딩

```c
#include <stdio.h>
int main() {
	int count = 0;
	char a[1000000];
	while (scanf("%s",&a[0]) == 1) {
		count++;
	}
	printf("%d",count);
}
```

```c
int main(){
	char s[1000000];
	int cnt;
	
	scanf("%[^\n]", s);
	
	if(s[0] == ' ') cnt = 0;
	else cnt = 1;
	
	for(int i=0;s[i]!='\0';i++)
		if(s[i] == ' ' && s[i+1] >= 'A')
			cnt++;
	
	printf("%d", cnt);
}
```

```c
int main(void) {
	char str[1000000];
	scanf("%[^\n]", str);
	int count = 0;
	char*ptr = strtok(str, " ");
	while (ptr != NULL){
		ptr = strtok(NULL, " ");
		count++;
	}
	printf("%d", count);
}
```