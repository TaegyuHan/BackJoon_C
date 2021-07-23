# 2442 별찍기 - 5

URL : [https://www.acmicpc.net/problem/2442](https://www.acmicpc.net/problem/2442)

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

void ShowStar(Star S)
{
    int len = S.number*2;
    int i, j, k;

    // 위부분
    for(i=0; i<=len; i+=2)
    {
        if(i==0) continue;
        
        for(j=0; j<(len/2) - (i/2); j++)
            printf(" ");

        for(k=1; k<i; k++)
            printf("*");

        if(i!=len) printf("\n");
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

숏 코딩

```c
/*************************************************************  
 * NOTE - 2442.c
        - https://www.acmicpc.net/problem/2442
 * Author - aegisduck
 * Since - 2019.07.02
**************************************************************/

#include <stdio.h>

void print_char(int n, char c);

int main(void){
    int n = 0;
    int cnt = 0;
    int w=0, s=0;

    scanf("%d", &n);
    cnt = 2*n - 1;
    for (int i=1; i<=n; i++){
        s = 2*i - 1;
        w = (cnt - s) / 2;

        print_char(w, ' ');
        print_char(s, '*');
 //       print_char(w, ' ');
        putchar('\n');
    }
    return 0;
}

void print_char(int n, char c){
    for (int i=0; i<n; i++){
        putchar(c);
    }
}
```

```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
        int num=0;
        int i=0, j=0, k=0;
        int space=0;
        scanf("%d", &num);

        space = (num*2-1)/2;
        for(i=0; i<num; i++)
        {
                for(j=0; j<space; j++)
                {
                        printf("%c", ' ');
                }
                for(k=0; k<(i+1)*2-1; k++)
                {
                        printf("%c", '*');
                }
                printf("\n");
                space--;
        }
        return 0;
}
```