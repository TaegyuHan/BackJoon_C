# 2108 통계학 x

URL : [https://www.acmicpc.net/problem/2108](https://www.acmicpc.net/problem/2108)

최빈값 수정만하면 완료

1 try

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

2 try

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define ARY_LEN 500001

typedef struct _Data 
{
	int inputDataCount;
	int sum;

	int modSameCount;
	int modIndex;
	int modResultArray[ARY_LEN];
} Data;

void inputIntData(int* num) { scanf("%d", num); return; }

// 퀵정렬
void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

int partition(int arr[], int low, int high)
{
	int pivot = arr[high];
	int i = (low - 1);
	for (int j = low; j <= high - 1; j++)
	{
		if (arr[j] <= pivot)
		{
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}

void quickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		int pi = partition(arr, low, high);
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

// 퀵정렬 end

void mean(Data* Data)
{
	printf("%d\n", (int)round((long double)Data->sum / (long double)Data->inputDataCount));
}

void median(Data* Data, int arr[])
{
	int index = Data->inputDataCount / 2;
	printf("%d\n", arr[index]);
}

void mod(Data* Data, int arr[])
{
	int i;
	int tmp,
		tmpCount = 0,
		tmpNum = 0;

	int result, 
		resultCount = 0;

	for (i = 0; i < Data->inputDataCount; i++)
	{
		// 처음 데이터
		if (i == 0)
		{
			Data->modIndex = 0;
			Data->modSameCount = 0;
			Data->modResultArray[Data->modIndex++] = arr[i];

			result = tmp = arr[i];
			resultCount = tmpCount = 1;
			continue;
		}

		// 같은 데이터 인지 확인
		if (tmp == arr[i]) // 같은 데이터
		{
			tmpCount++;
		}
		else // 다른 데이터
		{
			// 기존의 최빈값 비교
			if (resultCount < tmpCount)
			{
				result = arr[i - 1]; // 수정 i - 1
				resultCount = tmpCount;

				Data->modIndex = 0;
				Data->modSameCount = 0;
				Data->modResultArray[Data->modIndex++] = result;
			}
			// 같은 값
			else if (resultCount == tmpCount)
			{
				Data->modResultArray[Data->modIndex++] = arr[i];
				Data->modSameCount++;
			}

			tmp = arr[i];
			tmpCount = 1;
		}

	}
	
	if (Data->modSameCount > 0)
	{
		quickSort(Data->modResultArray, 0, Data->modSameCount);

		printf("Data->modSameCount : ");
		for (i = 0; i < Data->modSameCount; i++)
		{
			printf("%d ", Data->modResultArray[i]);
		}
	}
	else
	{
		printf("%d\n", result);
	}

	return;
}

void range(Data* Data, int arr[])
{ 
	int index = Data->inputDataCount;
	int result = arr[index  - 1] - arr[0];

	printf("%d\n", result);
}

int main(void)
{

	// 변수 선언
	Data* D = (Data*)malloc(sizeof(D));

	inputIntData(&(D->inputDataCount)); // 데이터 받는 횟수
	int* dataArray = (int*)malloc(sizeof(int) * (D->inputDataCount + 1));

	int i;
	D->sum = 0;
	for (i = 0; i < D->inputDataCount; i++)
	{
		inputIntData(&(dataArray[i]));
		D->sum += dataArray[i]; // 평균을 구하기 위한 합
	}

	// 퀵 정렬
	quickSort(dataArray, 0, D->inputDataCount - 1);

	printf("dataArray : ");
	for (i = 0; i < D->inputDataCount; i++)
	{
		printf("%d ", dataArray[i]);
	}
	printf("\n");

	// 평균
	mean(D);

	// 중앙값
	median(D, dataArray);

	// 최빈값
	mod(D, dataArray);

	//  범위
	range(D, dataArray);

	return 0;
}
```