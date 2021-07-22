# 11718 그대로 출력하기

URL : [https://www.acmicpc.net/problem/11718](https://www.acmicpc.net/problem/11718)

```c
#include <stdio.h>

int main(void)
{
    int a;
    while (1)
    {
        a = getchar();
        if( a == EOF) break;
        putchar(a);
    }
    return 0;
}
```

숏 코딩

```c
#include<stdio.h>

int main (void) {
	char ch[10000] = { 0, };

	for (int i = 0; i < 10000; i++) {
		scanf ("%c", &ch[i]);
		if (ch[i] == '\n' && ch[i - 1] == '\n')	break;
	}
	for (int i = 0; i < 10000; i++) {
		if (ch[i] == 0)	break;
		printf ("%c", ch[i]);
	}
	return 0;
}
```

```c
#include <stdio.h>
#include <string.h>
char a[101][101];
int main()
{
	int i;
	for ( i = 0; i < 100; i++)
	{
		gets(a[i]);
		if(a[i][0]==' ') break;
		if (a[i][strlen(a[i])-1] == ' ') break;
        if (a[i][0] == '\0') break;
		puts(a[i]);
	}

}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	char sentence;
	int num = 0;

	while (1)
	{
		if (scanf("%c", &sentence) == EOF)break;
		printf("%c", sentence);
		num++;
	}
}
```