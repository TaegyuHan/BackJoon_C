# 2675 문자열 반복

URL : [https://www.acmicpc.net/problem/2675](https://www.acmicpc.net/problem/2675)

```c
#include <stdio.h>

int main(void)
{
    unsigned short i; 
    unsigned char j, k;

    int count, RepeatNum; // 테스트 케이스의 개수, 케이스 반복 횟수
    char StringList[21]; // 문자열

    scanf("%d", &count);

    // 테스트 for 문
    for(i=0; i<count; i++)
    {
        scanf("%d %s", &RepeatNum, StringList);
        j=0;
        // 문자열 for 문
        for(j=0; StringList[j]!='\0'; j++)
        {   
            k=0;
            // 반복 for 문
            for(k=0; k<RepeatNum; k++){
                printf("%c", StringList[j]);
            }
        }
        printf("\n");
    }
    return 0;
}
```

숏 코드

```c
d,i,j;char c[21];
main(n){
	scanf("%d", &n);
	while (n--) {
		scanf("%d", &d);
		getchar();
		gets(c);
		for (i = 0; c[i] != '\0'; i++)
			for (j = 0; j < d; j++)
					printf("%c", c[i]);
		puts("");

	}
}
```

```c
main() {
	int c, l;
	char s[20], o;
	scanf("%d", &c);
	for(int i=0;i<c;i++)
	{
		scanf("%d %s", &l, &s);
		for(int j=0;s[j]!=0;j++)
			for(int k=0;k<l;k++)
				printf("%c", s[j]);
		printf("\n");
	}
}
```