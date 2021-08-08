# 2108 통계학

URL : [https://www.acmicpc.net/problem/2108](https://www.acmicpc.net/problem/2108)

최빈값 수정만하면 완료

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define TABLE_DATA 4001

#define TRUE 1
#define FALSE 0

int DATA_COUNT; // N(1 ≤ N ≤ 500,000)

typedef struct _Data
{
    int plus; 
    int minus; 
} Data;

typedef struct _Number
{   
    int* NumberArray; // 수가 들어갈 배열 
    int NumnerSum; // 수의 전체 합

    // 최빈값
    int modCount;
    int modIndex;
    int modType; // 1 : plus, 0 : minus
} Number;

Data IndexTable[TABLE_DATA] = {0, }; // 수의 개수가 들어갈 테이블

void merge(int data[], int left, int mid, int right)
{
    int i = left,
        j = mid + 1,
        k = left;

    int* temp = (int*)malloc(sizeof(int) * (DATA_COUNT + 1));

    while (i <= mid && j <= right)
    {
        if (data[i] <= data[j]) temp[k++] = data[i++];
        else temp[k++] = data[j++];
    }
    while (i <= mid) temp[k++] = data[i++];
    while (j <= right) temp[k++] = data[j++];
    for (int a = left; a <= right; a++) data[a] = temp[a];
}

void mergeSort(int data[], int left, int right)
{
    int mid;
    if (left < right)
    {
        mid = (left + right) / 2;
        mergeSort(data, left, mid);
        mergeSort(data, mid + 1, right);
        merge(data, left, mid, right);
    }
}


void InputIntData(int* num)
{
    scanf("%d", num);
}

void InsertDataToTable(Number* Number, int num)
{
    if (num >= 0)
    {
        (IndexTable[num].plus++);
        if (IndexTable[num].plus > Number->modCount)
        {
            Number->modCount++;
            Number->modIndex = num;
            Number->modType = 1;
        }
    }
    else
    {
        (IndexTable[num*-1].minus++);
        if (IndexTable[num * -1].minus > Number->modCount)
        {
            Number->modCount++;
            Number->modIndex = num;
            Number->modType = 0;
        }
    }
}

void mean(Number* Number)
{
    printf("%d\n", (int)round(Number->NumnerSum / (double)DATA_COUNT));
}

void median(Number* Number)
{
    int index = DATA_COUNT / 2;
    printf("%d\n", Number->NumberArray[index]);
}

void mod(Number* Number)
{
    printf("%d\n", Number->modIndex);
}

void range(Number* Number)
{
    int result = Number->NumberArray[DATA_COUNT - 1] - Number->NumberArray[0];
    printf("%d", result);
}

int main()
{
    int i;
    Number Number = {0, };

    Number.NumberArray = (int*)malloc(sizeof(int) * (DATA_COUNT + 1));

    // 수의 개수
    InputIntData(&DATA_COUNT);


    for (i = 0; i < DATA_COUNT; i++)
    {
        // 데이터 받기
        InputIntData(&Number.NumberArray[i]);

        // 합에 더하기
        Number.NumnerSum += Number.NumberArray[i];

        // table에 추가하기
        InsertDataToTable(&Number, Number.NumberArray[i]);
    }
    
    // 산술 평균
    mean(&Number);

    mergeSort(Number.NumberArray, 0, DATA_COUNT - 1);

    // 중앙값
    median(&Number);

    // 최빈값
    mod(&Number);

    // 범위
    range(&Number);

    return 0;
}
```