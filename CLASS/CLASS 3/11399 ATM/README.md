# 11399 ATM

URL : [https://www.acmicpc.net/problem/11399](https://www.acmicpc.net/problem/11399)

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1024

typedef struct _Heap
{
    int arr[MAX_N]; // N(1 ≤ N ≤ 1,000)
    int size;
    int inputDataSize;
} Heap;

void inputIntData(int* num) { scanf("%d", num); return; }

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void initHeap(Heap* hp)
{
    hp->size = 0;
}

void insert(Heap* hp, int data)
{
    int here = ++hp->size;

    while ((here != 1) && (data < hp->arr[here / 2]))
    {
        hp->arr[here] = hp->arr[here / 2];
        here /= 2;
    }
    hp->arr[here] = data;
}

int deleteData(Heap* hp)
{

    if (hp->size == 0) return -1;

    int ret = hp->arr[1];
    hp->arr[1] = hp->arr[hp->size--];
    int parent = 1;
    int child;

    while (1)
    {
        child = parent * 2;

        if (child + 1 <= hp->size && hp->arr[child] > hp->arr[child + 1])
            child++;

        if (child > hp->size || hp->arr[child] > hp->arr[parent])
            break;

        swap(&hp->arr[parent], &hp->arr[child]);
        parent = child;
    }

    return ret;

}

int MinComplete(Heap* H)
{
    int i;
    int resultSum = 0,
        backTmpSum = 0,
        TmpSum = 0;

    for (i = 0; i < H->inputDataSize; i++)
    {
        TmpSum = deleteData(H);
        backTmpSum += TmpSum;
        resultSum += backTmpSum;
    }

    return resultSum;
}

int main(void)
{
    Heap* H = (Heap*)malloc(sizeof(Heap));

    initHeap(H);

    int i;
    int tmp;

    inputIntData(&(H->inputDataSize));

    for (i = 0; i < H->inputDataSize; i++)
    {
        inputIntData(&tmp);
        insert(H, tmp);
    }

    printf("%d", MinComplete(H));

    return 0;
}
```

숏 코딩

퀵소트 풀이

```c
#include <stdio.h> 
#include <stdlib.h>
int compare(const void* a, const void* b)    // 오름차순 비교 함수 구현
{
	int num1 = *(int*)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	int num2 = *(int*)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1 < num2)    // a가 b보다 작을 때는
		return -1;      // -1 반환

	if (num1 > num2)    // a가 b보다 클 때는
		return 1;       // 1 반환

	return 0;    // a와 b가 같을 때는 0 반환
}

int main() {
	int n;
	int p[1000];
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &p[i]);
	}

	qsort(p, n, sizeof(int), compare);

	int sum = 0; 
	int result = 0;
	
	for (int i = 0; i < n; i++) {
		sum += p[i];
		result += sum;
	}

	printf("%d", result);
}
```

병합 정렬

```c
#include <stdio.h>

void MergeSort(int Array[], int m, int n);
void Merge(int Array[], int m, int middle, int n);

int sorted[1002];

int main(void) {
    int N, i, person[1001];
    long long sum, dp[1001];

    scanf("%d", &N);
    
    for (i = 1; i <= N; i++)
        scanf("%d", &person[i]);
    
    MergeSort(person, 1, N);
    
    dp[1] = person[1];
    sum = dp[1];
    
    for (i = 2; i <= N; i++) {
        dp[i] = dp[i - 1] + person[i];
        sum += dp[i];
    }
    
    printf("%lld\n", sum);
    
    return 0;
}

void MergeSort(int Array[], int m, int n) {
    int middle;
    
    if (m < n) {
        middle = (m + n) / 2;
        
        MergeSort(Array, m, middle);
        MergeSort(Array, middle + 1, n);
        
        Merge(Array, m, middle, n);
    }
}

void Merge(int Array[], int m, int middle, int n) {
    int i = m, j = middle + 1, k = m;
    
    while (i <= middle && j <= n) {
        if (Array[i] < Array[j]) {
            sorted[k] = Array[i];
            i++;
        } else {
            sorted[k] = Array[j];
            j++;
        }
        k++;
    }
    
    while (i <= middle)
        sorted[k++] = Array[i++];
    
    while (j <= n)
        sorted[k++] = Array[j++]; 
    
    for (i = m; i <= n; i++ )
        Array[i] = sorted[i];
}
```