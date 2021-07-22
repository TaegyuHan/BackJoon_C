# 11948 과목 선택

URL : [https://www.acmicpc.net/problem/11948](https://www.acmicpc.net/problem/11948)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct science
{
    int subject[4];
} Science;

typedef struct sociology
{   
    int subject[2];
} Sociology;

typedef struct testList
{
   Science Science;
   Sociology Sociology;
} TestList;

void bubbleSort(int list[], int len)
{
    int i, j;
    int temp;
    for(i=0; i<len; i++)
    {
        for(j=0; j<len; j++)
        {
            if(list[i] >= list[j])
            {
                temp = list[i];
                list[i] = list[j];
                list[j] = temp;
            }
        }
    }
}

void inputData(TestList * TL)
{
    scanf("%d %d %d %d %d %d",
        &TL->Science.subject[0],
        &TL->Science.subject[1],
        &TL->Science.subject[2],
        &TL->Science.subject[3],
        &TL->Sociology.subject[0],
        &TL->Sociology.subject[1] );
}

int pointSum(TestList TL)
{
    int i;
    int sum=0;
    for(i=0; i<3; i++)
    {
        sum += TL.Science.subject[i];
    }

    sum += (TL.Sociology.subject[0] > TL.Sociology.subject[1]) ? 
                TL.Sociology.subject[0] : TL.Sociology.subject[1];

    return sum;
}

int main(void)
{
    int result;
    TestList TL;

    inputData(&TL);
    bubbleSort(TL.Science.subject, 4);
    result = pointSum(TL);
    printf("%d", result);

    return 0;
}
```

숏 코딩

```c
#include<stdio.h>
int arr[6];
int main(void) {
	int i;
	int index1, index2;
	int min = 101;
	int sum = 0;
	for (i = 0; i < 6; i++) {
		scanf("%d", &arr[i]);
	}
	for (i = 0; i < 4; i++) {
		if (min > arr[i]) {
			min = arr[i];
			index1 = i;
		}
	}
	min = 101;
	for (i = 4; i < 6; i++)
	{
		if (min > arr[i]) {
			min = arr[i];
			index2 = i;
		}
	}
	for (i = 0; i < 6; i++) {
		if (i != index1 && i != index2)
			sum += arr[i];
	}
	printf("%d\n", sum);
}
```