# 2751 수 정렬하기 2

URL : [https://www.acmicpc.net/problem/2751](https://www.acmicpc.net/problem/2751)

```c
#include <stdio.h>

#define NUMBER_LEN 1000001

int DATA_COUNT;
int numberArray[NUMBER_LEN];
int tempArray[NUMBER_LEN];

void SCAN_DATA_COUNT()
{
    scanf("%d", &DATA_COUNT);
}

void InputDataToArray(int i)
{
    scanf("%d", &numberArray[i]);
}

void ShowDAtAFromArray(int i)
{
    printf("%d\n", numberArray[i]);
}

void merge(int data[], int left, int mid, int right) {
    int i = left,
        j = mid + 1,
        k = left;

    while (i <= mid && j <= right) {
        if (data[i] <= data[j]) tempArray[k++] = data[i++];
        else tempArray[k++] = data[j++];
    }
    while (i <= mid) tempArray[k++] = data[i++];
    while (j <= right) tempArray[k++] = data[j++];
    for (int a = left; a <= right; a++) data[a] = tempArray[a];
}

void mergeSort(int data[], int left, int right) {
    int mid;
    if (left < right) {
        mid = (left + right) / 2;
        mergeSort(data, left, mid);
        mergeSort(data, mid + 1, right);
        merge(data, left, mid, right);
    }
}

int main()
{
    int i;
    SCAN_DATA_COUNT();

    for (i = 0; i < DATA_COUNT; i++)
    {
        InputDataToArray(i);
    }

    mergeSort(numberArray, 0, DATA_COUNT - 1);

    for (i = 0; i < DATA_COUNT; i++)
    {
        ShowDAtAFromArray(i);
    }

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include<stdlib.h>
int compare(const void *a, const void *b);

int main()
{
	int sum = 0;
	int case_num;
	scanf("%d", &case_num);

	int *A_arr = malloc(sizeof(int) * case_num);
	for (int i = 0; i < case_num; i++)
	{
		scanf("%d", &A_arr[i]);
	}

	qsort(A_arr, case_num, sizeof(int), compare);
	for (int i = 0; i < case_num; i++)
	{
		printf("%d\n", A_arr[i]);
	}
}
int compare(const void *a, const void *b) 
{
	int num1 = *(int *)a;
	int num2 = *(int *)b;

	if (num1 < num2)
		return -1;

	if (num1 > num2) 
		return 1;

	return 0;
}
```