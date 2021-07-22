# 2440 별 찍기 - 3

URL : [https://www.acmicpc.net/problem/2440](https://www.acmicpc.net/problem/2440)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct star
{
    int number;
} Star;

void inputData(Star * S)
{   
    scanf("%d", &S->number);
    return;
}

void showStar(Star S)
{
    int i, j, k;
    int cnt = S.number;
    for(i=cnt; i>0; i--)
    {
        for(j=i; j>0; j--)
            printf("*");
        printf("\n");
    }
}

int main(void)
{
    Star S;
    inputData(&S);
    showStar(S);

    return 0;
}
```