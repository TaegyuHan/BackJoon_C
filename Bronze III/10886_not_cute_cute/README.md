# 10886 0 = not cute / 1 = cute

URL : [https://www.acmicpc.net/problem/10886](https://www.acmicpc.net/problem/10886)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct junHee
{
    int point;
} JunHee;

void inputData(JunHee * JunHee)
{
    scanf("%d", &JunHee->point);
}

void result(int cute, int ncute)
{
    (cute > ncute) ? 
        printf("Junhee is cute!") : printf("Junhee is not cute!");
}

int main(void)
{
    int i;
    int inputDataCount; // N (1 ≤ N ≤ 101, N은 홀수)
    int cute=0, ncute=0;
	JunHee JunHee;

    scanf("%d", &inputDataCount);

    for(i=0; i<inputDataCount; i++)
    {
        inputData(&JunHee);
        if(JunHee.point==1) cute += 1;
        else if(JunHee.point==0) ncute += 1;
    }

    result(cute, ncute);

    return 0;
}
```

숏코딩

```c
#include <stdio.h>

int main(void)
{
	int N;
	int num;
	int cute_count = 0;
	int else_count = 0;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &num);

		if (num == 1)
			cute_count++;
		else
			else_count++;
	}

	if (cute_count > else_count)
		printf("Junhee is cute!");
	else
		printf("Junhee is not cute!");

	return 0;
}
```