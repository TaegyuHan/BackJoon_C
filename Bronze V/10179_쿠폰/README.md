# 10179 쿠폰

URL : [https://www.acmicpc.net/problem/10179](https://www.acmicpc.net/problem/10179)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct mart
{
    double item;
} Mart;

void inputData(Mart * M)
{
    scanf("%lf", &M->item);
    return;
}

double sale(Mart M)
{
    double DiscountRate=0.8;
    return (M.item)*DiscountRate;
}

int main(void)
{
    int i, cnt;
    Mart M;

    scanf("%d", &cnt);

    for(i=0; i<cnt; i++)
    {
        inputData(&M);
        printf("$%.2lf\n", sale(M));
    }

    return 0;
}
```

숏 코딩

```c
int main()
{
    int n;
    scanf("%d", &n);

    double a;

    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &a);
        
        printf("$%.2lf\n", a * 0.8);
    }

    return 0;
}
```

```c
#include <stdio.h>
#include <math.h>

int main()
{
    int t;
    double price;

    scanf("%d",&t);

    for(int i = 0 ; i < t ; i++)
    {
        scanf("%lf",&price);
        printf("$%.2lf\n",round(price*0.8*100)/100);
    }

    return 0;
}
```