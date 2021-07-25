# 2010 플러그

URL : [https://www.acmicpc.net/problem/2010](https://www.acmicpc.net/problem/2010)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct plug
{
    int number;
} Plug;

void inputData(Plug * Plug)
{
    scanf("%d", &Plug->number);
}

int main(void)
{
    int i;
    int plugCount;
    int sum=1;
	Plug Plug;

    scanf("%d", &plugCount);

    for(i=0; i<plugCount; i++)
    {
        sum -= 1;
        inputData(&Plug);
        sum += Plug.number;
    }

    printf("%d", sum);

    return 0;
}
```