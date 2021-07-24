# 2522 별 찍기 12

URL : [https://www.acmicpc.net/problem/2522](https://www.acmicpc.net/problem/2522)

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
    int len = S.number*2;
    int i;
    int starNum = 1,
        spaceNum = S.number-1;

    for(i=1; i<len; i++)
    {
        space(spaceNum);
        star(starNum);
        if(i>=S.number)
        {
            starNum--;
            spaceNum++;
        }
        else 
        {
            starNum++;
            spaceNum--;
        }

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

숏 코딩

```c
#include <stdio.h>
int main(){
    
    int i, j, k, N;
    
    scanf("%d", &N);
    
    for(i = 1; i <= N; i++){
        for(j = 1; j <= N - i; j++){
            printf(" ");
        }

        for(k = 1; k <= i; k++){
            
            printf("*");
        }
        puts("");
    }
    for(i = 1; i <= N; i++){
        for(k = 1; k <= i; k++){
            
            printf(" ");
        }
        for(j = 1; j <= N - i; j++){
            
            printf("*");
        }
        puts("");
    }

}
```