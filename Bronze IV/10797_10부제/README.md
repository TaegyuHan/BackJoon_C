# 10797 10부제

URL : [https://www.acmicpc.net/problem/10797](https://www.acmicpc.net/problem/10797)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

struct CarList
{
    int carNumber[5];
};

int main(void)
{

    int i;
    int todayNumber;
    int resultNumber=0;
    struct CarList CarList;

    scanf("%d", &todayNumber);

    for(i=0; i<5; i++)
    {
        scanf("%d", &CarList.carNumber[i]);
        if(CarList.carNumber[i]==todayNumber) resultNumber++;
    }

    printf("%d", resultNumber);

	return 0;
}
```

숏코딩

```c
int num[5] = {};

int main()
{
	
	int X;
	int i;
	int count = 0;
	int tmp;

	scanf("%d", &X);

	if (X > 9 || 0 > X) {
		return 1;
	}

	for (i = 0; i < 5; i++) {
		scanf("%1d", &num[i]);

		tmp = num[i];

		if (tmp == X) {
			count += 1;
		}
	}
	
	printf("%d\n", count);
	
	return 0;
}
```

```c
#include <stdio.h>

int main(void)
{
	int num1;
	int car[5];
	int i, output =0;
	
	scanf("%d", &num1);
	scanf("%d %d %d %d %d", &(car[0]),  &(car[1]),  &(car[2]), &(car[3]),  &(car[4]));
	
	for(i=0 ; i< 5 ; i++)
	{
		if(car[i]== num1)
		{
			output ++;
		}
	}
	
	printf("%d\n", output);
	
	return 0;
}
```

```c
int main(void)
{
	int N, i;
	int car[5] = { 0, };
	int cnt = 0;

	scanf("%d", &N);

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &car[i]);
		if (car[i] == N) cnt++;
	}
	printf("%d", cnt);
}
```