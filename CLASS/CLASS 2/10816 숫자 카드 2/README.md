# 10816 숫자 카드 2

URL : [https://www.acmicpc.net/problem/10816](https://www.acmicpc.net/problem/10816)

```c
#include <stdio.h>

typedef struct _Table
{
    int plus;
    int minus;
} Table;

Table DataTable[10000001] = {0,};

void InputDataCnt(int* num)
{
    scanf("%d", num);
}

void InsertData()
{
    int index;

    scanf("%d", &index);

    if (index >= 0)
    {
        (DataTable[index].plus)++;
    }
    else
    {
        (DataTable[(index*-1)].minus)++;
    }
}

void ShowData(int i, int DATA_CNT)
{
    int index;

    scanf("%d", &index);

    if (index >= 0)
    {
        if(i != DATA_CNT)
            printf("%d ", DataTable[index].plus);
        else 
            printf("%d", DataTable[index].plus);
    }
    else
    {
        if (i != DATA_CNT)
            printf("%d ", DataTable[(index * -1)].minus);
        else
            printf("%d", DataTable[(index * -1)].minus);
    }
}

int main()
{
    int DATA_CNT; // 1 ≤ N ≤ 500,000
    int i;

    // 데이터 입력 받기
    InputDataCnt(&DATA_CNT);
    for (i = 0; i < DATA_CNT; i++)
    {
        InsertData();
    }

    // 데이터 확인 하기
    InputDataCnt(&DATA_CNT);
    for (i = 1; i <= DATA_CNT; i++)
    {
        ShowData(i, DATA_CNT);
    }

    return 0;
}
```

숏 코딩

```c
//숫자카드 2
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int narr[500002] = { 0, };
int n, m;
int lowerbount(int key)
{
	int left = 0;
	int right = n - 1;
	while (left < right)
	{
		int mid = (left + right) / 2;
		if (narr[mid] >= key)
			right = mid;
		else if(narr[mid]<key)
			left = mid + 1;
	}
	return right;
}

int upperBount(int key)
{
	int left = 0;
	int right = n - 1;
	while (left < right)
	{
		int mid = (left + right) / 2;
		if (narr[mid] <= key)
			left = mid + 1;
		else if (narr[mid] > key)
		{
			right = mid;
		}
	}
	if (key == narr[right])
	{
		right++;
	}
	return right;
}

int compare(const void* a, const void* b)
{
	int num1, num2;
	num1 = *(int*)a;
	num2 = *(int*)b;
	if (num1 > num2)
	{
		return 1;
	}
	if (num1 < num2)
		return -1;
	else
		return 0;
}
int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &narr[i]);
	}
	scanf("%d", &m);
	int* marr = (int*)malloc(sizeof(int) * m);
	
	
	qsort(narr, n, sizeof(int), compare);
	for (int i = 0; i < m; i++)
	{
		scanf("%d", &marr[i]);
		printf("%d ",upperBount(marr[i])-lowerbount(marr[i]));
	}
	free(marr);

	return 0;

}
```

```c
#include<stdio.h>

#define swap(type,x,y) do{type t=x ; x=y ; y=t;}while(0)

	int data[500001];
	int chk[20000003];

int main()
{
	int N,M;
	int i,j;

	scanf("%d",&N);

	for( i = 0 ; i < N ; i++)
	{
		scanf("%d",&data[i]);

		if(data[i]>=0)
		chk[data[i]]++;
		else
		chk[data[i]+20000000]++;
	}

	scanf("%d",&M);

	for( i = 0 ; i < M ; i++)
	{	
		int find_Num;
	
		scanf("%d",&find_Num);

				if(find_Num>=0)
				printf("%d ",chk[find_Num]);

				else 
				printf("%d ",chk[find_Num+20000000]);
			
		
		
	}

}
```