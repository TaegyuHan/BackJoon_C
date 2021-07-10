# 11651 좌표정럴하기 2

URL : [https://www.acmicpc.net/problem/11651](https://www.acmicpc.net/problem/11651)

버블 정렬

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int i, j, k;
    int temp; 
    int array[100000][2] = {0,};
    
    scanf("%d", &i);
    for(j=0; j<i; j++)
    {
        scanf("%d %d", &array[j][0], &array[j][1]);
    }

    printf("\n");

    for(j=0; j<i; j++)
    {
        for(k=i-1; k>0; k--)
        {
            if(array[k][1] < array[k-1][1] || 
              (array[k][1] == array[k-1][1] && array[k][0] < array[k-1][0]))
            {
                temp = array[k][1];
                array[k][1] = array[k-1][1];
                array[k-1][1] = temp;  
                
                temp = array[k][0];
                array[k][0] = array[k-1][0];
                array[k-1][0] = temp;               
            }
        }
        printf("%d %d\n", array[j][0], array[j][1]);
    }

    return 0;
}
```

병합정렬

```c
#include <stdio.h>
int array[100001][2] = {0,};
int tmp[100001][2]; // 새 배열

void mergeSort(int data[][2], int p, int r);
void merge(int data[][2], int p, int q, int r);

int main() {

    int i, n;

    scanf("%d", &n);

    for(i=0; i<n; i++)
    {
        scanf("%d %d", &array[i][0], &array[i][1]);
    }

     mergeSort(array, 0, n-1);

     for(i = 0; i < n; i++) {
         printf("%d %d\n", array[i][0], array[i][1]);
     }

  return 0;
}

void mergeSort(int data[][2], int p, int r) {
    int q;

    if(p<r) {
        q = (p+r)/2;
        mergeSort(data, p , q);
        mergeSort(data, q+1, r);
        merge(data, p, q, r);
    }
}

void merge(int data[][2], int p, int q, int r) {
    int i = p, j = q+1, k = p;
    while(i<=q && j<=r) {
        if(data[i][1] < data[j][1])
        {
            tmp[k][0] = data[i][0];
            tmp[k++][1] = data[i++][1];
        } 
        else if(data[i][1] == data[j][1] && data[i][0] < data[j][0])
        {
            tmp[k][0] = data[i][0];
            tmp[k++][1] = data[i++][1];
        }
        else
        {
            tmp[k][0] = data[j][0];
            tmp[k++][1] = data[j++][1];
        } 
    }
    while(i<=q)
    {
        tmp[k][0] = data[i][0];
        tmp[k++][1] = data[i++][1];
    } 
    while(j<=r)
    {
        tmp[k][0] = data[j][0];        
        tmp[k++][1] = data[j++][1];
    } 
    for(int a = p; a<=r; a++)
    {
        data[a][0] = tmp[a][0];        
        data[a][1] = tmp[a][1];
    } 
}
```

숏 코딩

```c
#include<stdio.h>
struct cd {
	int x;
	int y;
};
struct cd temp[100000];
struct cd xy[100000];
int isBig(struct cd a, struct cd b);
void partition(int start, int end);
void merge(int start, int middle, int end);
int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &xy[i].x, &xy[i].y);
	}

	//sorting
	partition(0, n - 1);

	for (int i = 0; i < n; i++) {
		printf("%d %d\n", xy[i].x, xy[i].y);
	}
	return 0;
}

void partition(int start, int end)
{

	if (start >= end) {
		return;
	}
	int middle = (start + end) / 2;
	partition(start, middle);
	partition(middle + 1, end);

	merge(start, middle, end);
}
void merge(int start, int middle, int end) {
	int left = start;
	int right = middle + 1;
	int index = start;
	while (left <= middle && right <= end) {
		if (isBig(xy[left], xy[right]) == 0) {
			temp[index] = xy[left];
			left++;
		}
		else if (isBig(xy[left], xy[right]) == 1) {
			temp[index] = xy[right];
			right++;
		}
		index++;
	}
	if (left > middle) {
		for (int i = right; i <= end; i++) {
			temp[index] = xy[i];
			index++;
		}
	}
	else {
		for (int i = left; i <= middle; i++) {
			temp[index] = xy[i];
			index++;
		}
	}
	for (int i = start; i <= end; i++) {
		xy[i] = temp[i];
	}
}

int isBig(struct cd a, struct cd b) {
	if (a.y == b.y) {
		if (a.x < b.x) {
			return 0;//a가 더 작음
		}
		else {
			return 1;
		}
	}
	else if (a.y < b.y) {
		return 0;
	}
	else {
		return 1;
	}
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

typedef struct point {
	int x;
	int y;
}point_t;

#define MAX_POINT (100000)
point_t point_list[MAX_POINT+10];

void quick_sort(point_t* arr, int left, int right)
{
	int i = left;
	int j = right;
	point_t pivot = arr[(i + j) / 2];
	point_t temp;

	// swap 할 조건
	// 왼쪽에 있는 나이가 더 크거나, 나이는 같은데  number 가 더 큰 경우

	// 오쪽에 있는 나이가 더 적거나, 나이는 같은데  number 가 더 작은 경우
	do {
		while (arr[i].y < pivot.y || (arr[i].y == pivot.y && arr[i].x < pivot.x)) {
			i++;
		}
		while (arr[j].y > pivot.y || (arr[j].y == pivot.y && arr[j].x > pivot.x)) {
			j--;
		}

		//swap
		if (i <= j) {
			temp = arr[j];
			arr[j] = arr[i];
			arr[i] = temp;
			i++;
			j--;
		}
	} while (i <= j);

	// left  
	if (left <= j) {
		quick_sort(arr, left, j);
	}

	// left  
	if (i <= right) {
		quick_sort(arr, i, right);
	}

	return;
}

int main()
{
	int N;
	int i;

//	freopen("input.txt", "r", stdin);
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d %d\n", &point_list[i].x, &point_list[i].y);
	}

	quick_sort(point_list, 0, N - 1);
	for (i = 0; i < N; i++) {
		printf("%d %d\n", point_list[i].x, point_list[i].y);
	}

	return 0;
}
```

```c
#include <stdio.h>

int arr[100000], brr[100000];
void quickSort(int* arr, int left, int right);
void swap(int* a, int* b);

int main() {

	int num;
	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%d %d", &brr[i], &arr[i]);
	}
	quickSort(arr, 0, num - 1);
	for (int i = 0; i < num; i++) {
		printf("%d %d\n", brr[i], arr[i]);
	}
	
	return 0;
}

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int* arr, int left, int right) {
	int pivot = (left + right) / 2, i = left - 1;
	swap(&arr[pivot], &arr[right]);
	swap(&brr[pivot], &brr[right]);

	for (int j = left; j < right; j++) {
		if (arr[j] < arr[right]) {
			i++;
			swap(&arr[j], &arr[i]);
			swap(&brr[j], &brr[i]);
		}
		else if (arr[j] == arr[right] && brr[j] < brr[right]) {
			i++;
			swap(&arr[j], &arr[i]);
			swap(&brr[j], &brr[i]);
		}
	}
	swap(&arr[i + 1], &arr[right]);
	swap(&brr[i + 1], &brr[right]);
	return i + 1;
}

void quickSort(int* arr, int left, int right) {
	if (left < right) {
		int pi = partition(arr, left, right);
		quickSort(arr, left, pi - 1);
		quickSort(arr, pi + 1, right);
	}
}
```