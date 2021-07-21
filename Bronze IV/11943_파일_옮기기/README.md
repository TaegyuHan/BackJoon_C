# 11943 파일 옮기기

URL : [https://www.acmicpc.net/problem/11943](https://www.acmicpc.net/problem/11943)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct basket
{
		int apple;  // (0 ≤ apple ≤ 1,000)
    int orange; // (0 ≤ orange ≤ 1,000)
} Basket;

int main(void)
{
    int i;
    int planA, planB;
    Basket BK[2];

    for(i=0; i<2; i++)
    {
        scanf("%d %d", &BK[i].apple, &BK[i].orange);
    }

    planA = BK[0].apple + BK[1].orange;
    planB = BK[1].apple + BK[0].orange;

    if(planA > planB)
        printf("%d", planB);
    else
        printf("%d", planA);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main() {
	int a,b,c,d;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	printf("%d", a+d>b+c ? b+c: a+d);
}
```

```c
#include <stdio.h>

int mymin(int a, int b);

int main(int argv, char** argc)
{
    int apple1, orange1;
    int apple2, orange2;
    int result = 0;
    
    scanf("%d %d ", &apple1, &orange1);
    scanf("%d %d ", &apple2, &orange2);
    
    result = mymin(apple1 + orange2, apple2 + orange1);
    printf("%d ", result);
}

int mymin(int a, int b)
{
    return (a < b ? a : b);
}
```

```c
#include <stdio.h>

int min(int a, int b)
{
	if(a<b)
		return a;
	return b;
}
void main()
{
	int first_apple, first_orange;
	int second_apple, second_orange;
	scanf("%d %d",&first_apple,&first_orange);
	scanf("%d %d",&second_apple,&second_orange);
	int sum1 = first_orange+second_apple;
	int sum2 = first_apple+second_orange;
	printf("%d\n",min(sum1,sum2));
}
```