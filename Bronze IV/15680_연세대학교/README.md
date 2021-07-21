# 15680 연세대학교

URL : [https://www.acmicpc.net/problem/15680](https://www.acmicpc.net/problem/15680)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct yonsei
{
	int type;
} YONSEI;

void print(YONSEI ys)
{
    if(ys.type==0)
        puts("YONSEI");
    else
        puts("Leading the Way to the Future");
}

int main(void)
{
    YONSEI Y;

    scanf("%d", &Y.type);
    print(Y);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main(){
	int N;
	scanf("%d", &N);
	if(N == 0) printf("YONSEI\n");
	else if(N == 1) printf("Leading the Way to the Future\n");
}
```

```c
#include <stdio.h>
int main()
{
	int flag;

	scanf("%d", &flag);

	if (flag == 0)
		printf("YONSEI");
	else
		printf("Leading the Way to the Future");
}
```