# 17362 수학은 체육과목 입니다 2

URL : [https://www.acmicpc.net/problem/17362](https://www.acmicpc.net/problem/17362)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct problem
{
    int inputNum; // (1 ≤ n ≤ 10^9)

} Problem;

void problemSolving(Problem * P)
{
    int startNumber = P->inputNum - 6;
    int fingerCount = startNumber%4;
    int direction = (startNumber/4)%2; // 0은 왼쪽 < , 1은 오른쪽 > 

    if(P->inputNum <= 5)
        printf("%d", P->inputNum);
    else
    {
        if(direction==0) // 왼쪽
        {
            printf("%d", 4 - fingerCount);
        }
        else if (direction==1) // 오른쪽
        {
            printf("%d", 2 + fingerCount);
        }
    }
}

int main(void)
{
    Problem P;
    scanf("%d", &P.inputNum);
    problemSolving(&P);

    return 0;
}
```

숏코딩

```c
#include<stdio.h>

int main() 
{
    long long n;
    scanf("%lld", &n);
    
    switch (n % 8)
    {
        case 1:
            printf("1");
            break;
        case 2:
            printf("2");
            break;
        case 3:
            printf("3");
            break;
        case 4:
            printf("4");
            break;
        case 5:
            printf("5");
            break;
        case 6:
            printf("4");
            break;
        case 7:
            printf("3");
            break;
        default:
            printf("2");
    }
    return 0;
}
```

```c
#include<stdio.h>

int main()
{
	int n, tp, local;
	scanf("%d", &n);
	if((n%8)>5)
    {
        local=10-n%8;
    }
    else if((n%8)==0)
    {
        local=2;
    }
    else
    {
        local=n%8;
    }
	
    printf("%d", local);
}
```