# 10989 수 정렬하기 3

URL : [https://www.acmicpc.net/problem/10989](https://www.acmicpc.net/problem/10989)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRY_LEN 10001

typedef struct _Data
{
	int len;
	int CountTable[ARRY_LEN];
} Data;

void InputIntData(int* num)
{
	scanf("%d", num);
}

void Count(Data* D, int num)
{
	(D->CountTable[num])++;
}

void CountPrint(Data* D, int num)
{
	int i;
	for (i = 0; i < D->CountTable[num]; i++)
		printf("%d\n", num);
}

int main(void)
{
	int i;
	int tempNum;
	Data* D = (Data*)malloc(sizeof(Data));
	memset(D, 0, sizeof(Data));

	InputIntData(&(D->len));

	for (i = 0; i < D->len; i++)
	{
		InputIntData(&tempNum);
		Count(D, tempNum);
	}

	for (i = 0; i < ARRY_LEN; i++)
	{
		if ((D->CountTable[i]) != 0)
			CountPrint(D, i);
	}

	free(D);

	return 0;
}
```

숏 코딩

```c
#include<stdio.h>
void counting(int *arr, int len);
int main()
{
	int arr[100000]={0};
	int len=0;
	scanf("%d", &len);
	counting(arr,len);
	int j=0;
	while(j<100000)
	{	
		int k=0;
		while(k<*(arr+j))
		{
			printf("%d\n", j+1);
			k++;
		}
		j++;
	}
	return 0;
}
void counting(int *arr, int len)
{
	int i=0;
	int num=1;
	while(i<len)
	{
		scanf("%d", &num);
		*(arr+num-1)=*(arr+num-1)+1;
		i++;
	}
}
```

```c
#include <stdio.h>

#define size 10001

int main(void)
{
	int n, num, cnt[size];

	scanf("%d", &n);

	for (int i = 0; i < size; i++)//초기화
		cnt[i] = 0;

	for (int i = 0; i < n; i++)//카운팅
	{
		scanf("%d", &num);
		cnt[num]++;
	}

	for (int i = 0; i < size; i++)//출력
	{
		if (cnt[i] == 0)
			continue;

		for (int j = 0; j < cnt[i]; j++)
			printf("%d\n", i);
	}

	return 0;
}
```