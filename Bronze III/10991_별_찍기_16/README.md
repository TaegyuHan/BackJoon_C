# 10991 별 찍기 16

URL : [https://www.acmicpc.net/problem/10991](https://www.acmicpc.net/problem/10991)

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
}

void star(int n)
{
    for(int i=0; i<n; i++)
        printf("*");
}

void space(int n)
{
    for(int i=0; i<n; i++)
        printf(" ");
}

void ShowStar(Star S)
{
    int len = S.number;
    int i, j;
    int type, // 1:별  0:빈공간
        spaceNum = S.number-1;
    int drawCount = 1;

    for(i=0; i<len; i++)
    {
        type=1;
        space(spaceNum);
        for(j=0; j<drawCount; j++)
        {
            if(type==1) {star(1); type=0;}
            else if(type==0) {space(1); type=1;}
        }
        spaceNum--;
        drawCount +=2;
        if(i!=len-1) printf("\n");
    }
}

int main(void)
{
    Star S;
    inputData(&S);
    ShowStar(S);

    return 0;
}
```